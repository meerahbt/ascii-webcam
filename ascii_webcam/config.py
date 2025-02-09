import shutil
import os

class Config:
    def __init__(self):
        self.DEFAULT_DEVICE_ID = 0
        self.CURSOR_HIDE = "\033[?25l"
        self.CURSOR_SHOW = "\033[?25h"
        
    @staticmethod
    def get_terminal_size():
        """Get current terminal size"""
        columns, rows = shutil.get_terminal_size()
        return columns, rows

    @staticmethod
    def move_cursor(x, y):
        """Move cursor to specific position"""
        return f"\033[{y};{x}H"

    @staticmethod
    def clear_screen():
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')