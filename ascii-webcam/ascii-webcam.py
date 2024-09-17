import cv2
import numpy as np

# capturing the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Process the frame here
    # ASCII Conversion

small_frame = cv2.resize(frame, (80, 60))  # Adjust these dimensions as needed
gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)

    
# Get the dimensions of the frame
height, width = gray.shape

ascii_chars = [' ', '.', "'", '`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '>', '<', '~', '+', '_', '-', '?', ']', '[', '}',
            '{', '1', ')', '(', '|', '\\', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L',
            'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']
    

for y in range(0, height, 2):  # Step by 2 to reduce vertical resolution
    for x in range(width):
        # Get the grayscale value of the pixel
        pixel_value = gray[y, x]
        
        # Map the pixel value to an ASCII character
        ascii_char = ascii_chars[int(pixel_value / 255 * (len(ascii_chars) - 1))]
        
        # Append the character to the ASCII art string
        ascii_art += ascii_char

# Add a newline at the end of each row
ascii_art += "\n"

# Print or display the ASCII art
print(ascii_art)


# Break the loop if 'q' is pressed; not sure if this is what I want as part of it yet 
#if cv2.waitKey(1) & 0xFF == ord('q'):
 #   break

cap.release()
cv2.destroyAllWindows()