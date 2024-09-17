import cv2
import numpy as np
import os

# ASCII characters from dark to light
ascii_chars = [' ', '.', "'", '`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '>', '<', '~', '+', '_', '-', '?', ']', '[', '}',
               '{', '1', ')', '(', '|', '\\', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L',
               'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']

def convert_to_ascii(frame, cols=80, rows=60):
    # Resize the frame
    small_frame = cv2.resize(frame, (cols, rows))
    
    # Convert to grayscale
    gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    
    # Convert each pixel to ASCII
    ascii_art = ""
    for row in gray:
        for pixel in row:
            ascii_art += ascii_chars[int(pixel / 255 * (len(ascii_chars) - 1))]
        ascii_art += "\n"
    
    return ascii_art

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
        
        # Convert frame to ASCII
        ascii_frame = convert_to_ascii(frame)
        
        # Clear console and print ASCII art
        clear_console()
        print(ascii_frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()