class ArabicConverter:
    def __init__(self):
        # Arabic characters from densest to lightest visual weight
        self.arabic_chars = [
            'ع', 'غ', 'ح', 'خ', 'ه', 'ة',
            'ص', 'ض', 'ط', 'ظ', 'س', 'ش',
            'ي', 'ب', 'ت', 'ث', 'ن',
            'م', 'ك', 'ل', 'ا', 'إ', 'أ',
            'و', 'ؤ', 'ر', 'ز', 'د', 'ذ',
            'ف', 'ق', '،', '؛', ' '
        ]

    def convert_to_arabic(self, processed_frame):
        height, width = processed_frame.shape
        result = []
        for y in range(height):
            line = ''
            for x in range(width):
                pixel_value = processed_frame[y, x]
                char_index = int(pixel_value / 255 * (len(self.arabic_chars) - 1))
                line += self.arabic_chars[char_index]
            result.append(line)
        return ''.join(f"{line}" for line in result)