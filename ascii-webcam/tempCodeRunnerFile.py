    for x in range(width):
            # Get the grayscale value of the pixel
            pixel_value = gray[y, x]
            
            # Map the pixel value to an ASCII character
            ascii_char = ascii_chars[int(pixel_value / 255 * (len(ascii_chars) - 1))]
            
            # Append the character to the ASCII art string
            ascii_art 