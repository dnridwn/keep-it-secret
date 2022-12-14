class Secret:
    def __init__(self, text):
        self._text = text

    def encrypt(self):
        result = ''
        for char in list(self._text):
            char = chr((ord(char) << 1) + 50)
            result += char
        return result

    def decrypt(self):
        result = ''
        for char in list(self._text):
            char = chr((ord(char) - 50) >> 1)
            result += char
        return result
