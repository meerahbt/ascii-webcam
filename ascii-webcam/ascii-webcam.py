import cv2
import numpy as np
import os

# Expanded Unicode blocks for more detailed shading
unicode_blocks = [
    '\u2588', '\u2587', '\u2586', '\u2585', '\u2584', 
    '\u2583', '\u2582', '\u2581', '\u2003'
]

def convert_to_blocks(frame, cols, rows):
    # Resize the frame
    small_frame = cv2.resize(frame, (cols, rows))
    
    # Convert to grayscale
    gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    
    # Convert each pixel to a block
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
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1600)

    # Calculate the number of columns and rows for the ASCII art
    # We'll scale down by a factor to maintain performance
    scale_factor = 0.05  # Adjust this value to change the level of detail
    cols = int(2560 * scale_factor)
    rows = int(1600 * scale_factor)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert frame to block art
        block_frame = convert_to_blocks(frame, cols, rows)
        
        # Clear console and print block art
        clear_console()
        print(block_frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()