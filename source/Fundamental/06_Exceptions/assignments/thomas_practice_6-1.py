"""
Practicing reading and writing files in Python.
"""

def write_file():
    """
    Writes a file named my_name.txt with two names and an age.
    """
    try:
        filename = open('my_name.txt', 'w')
        filename.write('Christian Thomas')
        filename.write('\nBruce Wayne')
        filename.write('\n30')

        filename.close()
    except IOError:
        print('An error occurred trying to write to the file.')
    else:
        print('File written successfully.')

def read_file():
    """Reads the my_name.txt file and displays the names and age on the screen."""
    try:
        filename = open('my_name.txt', 'r')
        name1 = filename.readline().rstrip()
        name2 = filename.readline().rstrip()
        age = int(filename.readline().rstrip())
        filename.close()
    except IOError:
        print('An error occurred trying to read the file.')
    else:
        print(f'Name 1: {name1}')
        print(f'Name 2: {name2}')
        print(f'Age: {age}')
        print(f'Age divided by 2: {age / 2}')

def main():
    write_file()
    read_file()

if __name__ == '__main__':
    main()