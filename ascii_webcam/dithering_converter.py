class DitheringConverter:
    def __init__(self):
        # Braille patterns from darkest to lightest
        self.dither_chars = [
            '⣿', '⢯', '⢕', '⢅', '⢁', '⠡', '⠑', '⠁',
            '⡿', '⢷', '⢓', '⢃', '⠃', '⠣', '⠒', ' '
        ]

    def convert_to_dither(self, processed_frame):
        height, width = processed_frame.shape
        result = []
        for y in range(height):
            line = ''
            for x in range(width):
                pixel_value = processed_frame[y, x]
                char_index = int(pixel_value / 255 * (len(self.dither_chars) - 1))
                line += self.dither_chars[char_index]
            result.append(line)
        return ''.join(f"{line}" for line in result)

    def convert_to_ordered_dither(self, processed_frame):
        return self.convert_to_dither(processed_frame)