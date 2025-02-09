# ascii_converter.py
class ASCIIConverter:
    def __init__(self):
        self.unicode_blocks = [
            '\u2588',  # Full block
            '\u2593',  # Dark shade
            '\u2592',  # Medium shade
            '\u2591',  # Light shade
            ' '        # Space (for empty/lightest)
        ]

# ASCIIConverter
    def convert_to_blocks(self, processed_frame):
        result = []
        for row in processed_frame:
            line = ''
            for pixel in row:
                index = int(pixel / 255 * (len(self.unicode_blocks) - 1))
                line += self.unicode_blocks[index]
            result.append(line)
        return ''.join(f"{line}" for line in result)
    

