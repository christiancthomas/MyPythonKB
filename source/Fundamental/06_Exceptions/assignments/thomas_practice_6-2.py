"""
This program writes the numbers 50 to 100 to a file and then reads the file to display the numbers.
"""

def write_file():
    """Writes an output file with the filename number_list.txt"""
    try:
        filename = open('number_list.txt', 'w')
        for i in range(50, 101):
            filename.write(f'{i}\n')
        filename.close()
    except IOError:
        print('An error occurred trying to write to the file.')
    else:
        print('File written successfully.')

def read_file():
    """Reads the number_list.txt file and displays the numbers on the screen."""
    try:
        filename = open('number_list.txt', 'r')
        for line in filename:
            print(line.rstrip())
        filename.close()
    except IOError:
        print('An error occurred trying to read the file.')
    else:
        print('File read successfully.')

def main():
    write_file()
    read_file()

if __name__ == '__main__':
    main()
