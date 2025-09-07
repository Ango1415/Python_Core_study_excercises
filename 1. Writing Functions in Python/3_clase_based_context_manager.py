class MyFileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f"File: '{self.filename}' has been opened in : '{self.mode}' mode")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print(f"File: '{self.filename}' has been closed")
        if exc_type:
            print(f"An exception ocurred: {exc_value}")
            # Returning False (or None) allows the exception to propagate, True if not
            return False


if __name__ == '__main__':
    with MyFileContextManager('MyFile.txt', 'r') as f:
        print(f.read())

    try:
        with MyFileContextManager('MyFile_2.txt', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print('Error caught as expected')