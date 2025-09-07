import contextlib
import os

@contextlib.contextmanager
def in_dir(path):
    # Save current directory
    old_dir = os.getcwd()
    # Switching to the new working directory
    os.chdir(path)

    yield
    # Change back to the original working directory
    os.chdir(old_dir)

if __name__ == '__main__':
    print(os.getcwd())
    print(os.listdir())

    with in_dir("C:\\Users\\USUARIO\\OneDrive\\Desktop\\Python Study - EPAM\\code"):
        print(os.getcwd())
        print(os.listdir())
        with open('NewTestFile.txt', 'w+') as file:
            file.write('Hi, this is the test of the os.chdir code...\n')
            file.write('File txt created and edited successfully!\n')

    print(os.getcwd())
    print(os.listdir())

    with in_dir("C:\\Users\\USUARIO\\OneDrive\\Desktop\\Python Study - EPAM\\code"):
        with open('NewTestFile.txt', 'r') as file:
            print(file.read())
