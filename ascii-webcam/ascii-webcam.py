import cv2
import numpy as np
import os
import shutil

# Unicode blocks for different shades (from darkest to lightest)
unicode_blocks = [
    '\u2588',  # Full block
    '\u2593',  # Dark shade
    '\u2592',  # Medium shade
    '\u2591',  # Light shade
    '\u2580',  # Upper half block
    '\u2584',  # Lower half block
    '\u258c',  # Left half block
    '\u2590',  # Right half block
    '\u2003'   # Em space (for empty space)
]

def get_terminal_size():
    columns, rows = shutil.get_terminal_size()
    return columns, rows

def convert_to_blocks(frame, cols, rows):
    # Resize the frame to fit the terminal
    aspect_ratio = frame.shape[1] / frame.shape[0]
    new_width = cols
    new_height = int(new_width / aspect_ratio)
    if new_height > rows:
        new_height = rows
        new_width = int(new_height * aspect_ratio)
    
    small_frame = cv2.resize(frame, (new_width, new_height))
    
    # Flip the frame horizontally
    small_frame = cv2.flip(small_frame, 1)
    
    # Convert to grayscale
    gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    
    # Convert each pixel to a Unicode block
    block_art = ""
    for row in gray:
        for pixel in row:
            index = int(pixel / 255 * (len(unicode_blocks) - 1))
            block_art += unicode_blocks[index]
        block_art += "\n"
    
    return block_art

def clear_console():
    # Clear console command for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Capturing the webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Get current terminal size
        cols, rows = get_terminal_size()
        
        # Convert frame to block art
        block_frame = convert_to_blocks(frame, cols, rows - 1)  # Subtract 1 to avoid scrolling
        
        # Clear console and print block art
        clear_console()
        print(block_frame, end='')
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()