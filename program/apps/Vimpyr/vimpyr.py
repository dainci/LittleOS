# vimpyr V3

import sys
import tty
import termios


class Vimpyr:
    def __init__(self):
        self.lines = []
        self.cursor_x = 0
        self.cursor_y = 0

    def run(self):
        self.set_terminal_raw_mode()
        self.display()
        while True:
            char = self.get_keypress()
            self.process_keypress(char)

    def display(self):
        for i, line in enumerate(self.lines):
            if i == self.cursor_y:
                print(f"> {line}")
            else:
                print(f"  {line}")
        self.display_shortcuts()

    def display_shortcuts(self):
        print("Keyboard Shortcuts:")
        print("  - Ctrl + Q: Quit")
        print("  - Ctrl + S: Save and Quit")
        print("  - Arrow keys: Move cursor")
        print("  - Enter: Insert new line")
        print("  - Backspace: Delete character")

    def get_keypress(self):
        return sys.stdin.read(1)

    def process_keypress(self, char):
        if char == "\x11":  # Ctrl + Q
            self.exit()
        elif char == "\x13":  # Ctrl + S
            self.save_and_exit()
        elif char == "\x1b":  # Escape key
            self.process_escape_sequence()
        elif char == "\n":  # Enter key
            self.insert_newline()
        elif char == "\b":  # Backspace key
            self.delete_character()
        else:
            self.insert_character(char)

    def process_escape_sequence(self):
        escape_sequence = sys.stdin.read(2)
        if escape_sequence == "[A":  # Up arrow
            self.move_up()
        elif escape_sequence == "[B":  # Down arrow
            self.move_down()
        elif escape_sequence == "[C":  # Right arrow
            self.move_right()
        elif escape_sequence == "[D":  # Left arrow
            self.move_left()

    def insert_newline(self):
        line = self.lines[self.cursor_y]
        prefix = line[:self.cursor_x]
        suffix = line[self.cursor_x:]
        new_line = prefix
        self.lines[self.cursor_y] = new_line
        self.cursor_x = 0
        self.cursor_y += 1
        self.lines.insert(self.cursor_y, suffix)

    def delete_character(self):
        line = self.lines[self.cursor_y]
        if self.cursor_x > 0:
            new_line = line[: self.cursor_x - 1] + line[self.cursor_x :]
            self.lines[self.cursor_y] = new_line
            self.cursor_x -= 1
        elif self.cursor_y > 0:
            prev_line = self.lines[self.cursor_y - 1]
            prev_line_length = len(prev_line)
            new_line = prev_line + line
            self.lines[self.cursor_y - 1] = new_line
            self.cursor_x = prev_line_length
            self.cursor_y -= 1
            self.lines.pop(self.cursor_y + 1)

    def insert_character(self, char):
        line = self.lines[self.cursor_y]
        new_line = line[:self.cursor_x] + char + line[self.cursor_x :]
        self.lines[self.cursor_y] = new_line
        self.cursor_x += 1

    def move_up(self):
        if self.cursor_y > 0:
            self.cursor_y -= 1
            if self.cursor_x >= len(self.lines[self.cursor_y]):
                self.cursor_x = len(self.lines[self.cursor_y]) - 1

    def move_down(self):
        if self.cursor_y < len(self.lines) - 1:
            self.cursor_y += 1
            if self.cursor_x >= len(self.lines[self.cursor_y]):
                self.cursor_x = len(self.lines[self.cursor_y]) - 1

    def move_left(self):
        if self.cursor_x > 0:
            self.cursor_x -= 1

    def move_right(self):
        if self.cursor_x < len(self.lines[self.cursor_y]):
            self.cursor_x += 1

    def save_and_exit(self):
        self.reset_terminal_mode()
        filename = input("Enter the filename to save: ")
        try:
            with open(filename, "w") as file:
                file.write("\n".join(self.lines))
            print(f"File '{filename}' saved.")
        except Exception as e:
            print(f"Error saving the file: {str(e)}")
        sys.exit()

    def exit(self):
        self.reset_terminal_mode()
        sys.exit()

    def set_terminal_raw_mode(self):
        tty.setraw(sys.stdin.fileno())

    def reset_terminal_mode(self):
        termios.tcsetattr(sys.stdin, termios.TCSAFLUSH, self.get_terminal_attributes())

    @staticmethod
    def get_terminal_attributes():
        return termios.tcgetattr(sys.stdin)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            with open(filename, "r") as file:
                lines = file.read().splitlines()
                editor = Vimpyr()
                editor.lines = lines
                editor.run()
        except Exception as e:
            print(f"Error opening the file: {str(e)}")
    else:
        print("Please provide a filename as a command-line argument.")
