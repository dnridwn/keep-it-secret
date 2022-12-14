import os

class FileHandler:
    def __init__(self, file_name):
        self._folder_name = 'files'
        self._file_extension = 'drs'
        self._file_name = file_name
        self._file_path = self._folder_name + '/' + self._file_name + '.' + self._file_extension

    def is_exists(self):
        return os.path.isfile(self._file_name)

    def create(self):
        f = open(self._file_path, 'x')
        f.close()

    def write(self, text):
        if self.is_exists():
            return
        f = open(self._file_path, 'a')
        f.write(text)
        f.close()

    def read(self, text):
        f = open(self._file_path, 'r')
        text = f.read()
        f.close()
        return text

    def delete(self):
        if not self.is_exists():
            return
        os.remove(self._file_path)