def copy(src, dst):
    """
    Example of nested context manager functions, this func copies the content of the
    source file into de destination file
    Args:
        src: Source file where we're going to extract the desired content.
        dst: Destination file where we're going to save the extracted data.

    Returns:
        None
    """
    # Open both files
    with open(src, 'r') as f_src:
        with open(dst, 'w') as f_dst:
            # Read and write each line, one at a time
            for line in f_src:
                f_dst.write(line)

def print_(src, dst):
    """
        Example of nested context manager functions, this func prints the content of the
        source and destination files
        Args:
            src: Source file where we extracted the desired content.
            dst: Destination file where we saved the extracted data.

        Returns:
            None
        """
    # Open both files
    with open(src, 'r') as f_src:
        with open(dst, 'r') as f_dst:
            # Read both files
            print('Source file: ')
            print(f_src.read())
            print('\nDestination file: ')
            print(f_dst.read())

if __name__ == '__main__':
    src_file = 'MyFile.txt'
    dst_file = 'MyFile_2.txt'

    copy('MyFile.txt', 'MyFile_2.txt')
    print_('MyFile.txt', 'MyFile_2.txt')