import cv2
import numpy as np
import os

# Extended list of Unicode blocks for more detailed shading (from darkest to lightest)
unicode_blocks = [
    '\u2588',  # Full block
    '\u2593',  # Dark shade
    '\u2592',  # Medium shade
    '\u2591',  # Light shade
    '\u258c',  # Left half block
    '\u2590',  # Right half block
    '\u2580',  # Upper half block
    '\u2584',  # Lower half block
    '\u258e',  # Left quarter block
    '\u258a',  # Left three quarters block
    '\u2596',  # Quadrant lower left
    '\u2597',  # Quadrant lower right
    '\u2598',  # Quadrant upper left
    '\u259d',  # Quadrant upper right
    '\u259a',  # Quadrant upper left and lower right
    '\u259e',  # Quadrant upper right and lower left
    '\u2599',  # Quadrant upper left and lower left and lower right
    '\u259b',  # Quadrant upper left and upper right and lower left
    '\u259c',  # Quadrant upper left and upper right and lower right
    '\u259f',  # Quadrant upper right and lower left and lower right
    '\u2581',  # Lower one eighth block
    '\u2582',  # Lower one quarter block
    '\u2583',  # Lower three eighths block
    '\u2585',  # Lower five eighths block
    '\u2586',  # Lower three quarters block
    '\u2587',  # Lower seven eighths block
    '\u2003'   # Em space (for empty space)
]

def convert_to_blocks(frame, cols, rows):
    # Resize the frame
    small_frame = cv2.resize(frame, (cols, rows))
    
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
    
    # Set capture resolution to match MacBook's 16:10 aspect ratio
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2)