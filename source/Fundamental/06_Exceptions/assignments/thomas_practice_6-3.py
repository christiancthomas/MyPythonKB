"""
This program reads a file named students.txt, which contains student names and their scores.
It displays the names and scores in a formatted manner.
"""

def main():
    """Reads the students.txt file and displays the names on the screen."""
    # Print header before reading file
    print("Name \t\tScore")
    print("-" * 32)

    try:
        with open('students.txt', 'r') as filename:
            lines = filename.readlines()
            # This processes pairs of lines (name followed by score)
            for i in range(0, len(lines), 2):
                if i+1 < len(lines):
                    name = lines[i].strip()
                    score = lines[i+1].strip()
                    print(f'{name} \t{score}')
    except IOError:
        print('An error occurred trying to read the file.')
    else:
        print('File read successfully.')

if __name__ == '__main__':
    main()