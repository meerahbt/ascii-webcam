import cv2
import numpy as np
import os
import shutil
import sys

# Simplified set of Unicode blocks for different shades (from darkest to lightest)
unicode_blocks = [
    '\u2588',  # Full block
    '\u2593',  # Dark shade
    '\u2592',  # Medium shade
    '\u2591',  # Light shade
    ' '        # Space (for empty/lightest)
]

def get_terminal_size():
    columns, rows = shutil.get_terminal_size()
    return columns, rows

def convert_to_blocks(frame, cols, rows):
    # Resize the frame to fit the terminal
    aspect_ratio = frame.shape[1] / frame.shape[0]
    new_width = cols
    new_height = int(new_width / aspect_ratio / 2)  # Divide by 2 to account for character aspect ratio
    if new_height > rows:
        new_height = rows
        new_width = int(new_height * aspect_ratio * 2)
    
    small_frame = cv2.resize(frame, (new_width, new_height))
    
    # Flip the frame horizontally
    small_frame = cv2.flip(small_frame, 1)
    
    # Convert to grayscale
    gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    
    # Enhance contrast
    gray = cv2.equalizeHist(gray)
    
    # Convert each pixel to a Unicode block
    block_art = ""
    for row in gray:
        for pixel in row:
            index = int(pixel / 255 * (len(unicode_blocks) - 1))
            block_art += unicode_blocks[index]
        block_art += "\n"
    
    return block_art

def move_cursor(x, y):
    print(f"\033[{y};{x}H", end="")

def main():
    # Capturing the webcam
    cap = cv2.VideoCapture(0)
    
    # Clear the console once at the start
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Hide the cursor
    print("\033[?25l", end="")
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Get current terminal size
            cols, rows = get_terminal_size()
            
            # Convert frame to block art
            block_frame = convert_to_blocks(frame, cols, rows - 1)  # Subtract 1 to avoid scrolling
            
            # Move cursor to top-left corner and print block art
            move_cursor(0, 0)
            sys.stdout.write(block_frame)
            sys.stdout.flush()
            
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    finally:
        # Show the cursor again
        print("\033[?25h", end="")
        
        # Release the capture and close windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()