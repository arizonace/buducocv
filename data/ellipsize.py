# azce::ellipsize.py - Arizona Edwards
# Created: 2024-11-30 10:13-EST

class ellipsize:
    @staticmethod
    def left(text, max_length, ellipsis='...'):
        if len(text) <= max_length:
            return text
        return text[:max_length - len(ellipsis)] + ellipsis

    @staticmethod
    def right(text, max_length, ellipsis='...'):
        if len(text) <= max_length:
            return text
        return ellipsis + text[-(max_length - len(ellipsis)):]

    @staticmethod
    def center(text, max_length, ellipsis='...'):
        if len(text) <= max_length:
            return text
        left_len = (max_length - len(ellipsis)) // 2
        right_len = max_length - len(ellipsis) - left_len
        return text[:left_len] + ellipsis + text[-right_len:]

    @staticmethod
    def mid(text, left, right, ellipsis='...'):
        if len(text) <= left + right + len(ellipsis):
            return text
        return text[:left] + ellipsis + text[-right:]
