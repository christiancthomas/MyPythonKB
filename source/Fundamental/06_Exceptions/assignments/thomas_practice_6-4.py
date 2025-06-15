"""
Reads the number_list.txt file, created for the previous assignment, and calculates the sum and average of the numbers.
"""

def main():
    filename = open('number_list.txt', 'r')
    number_list = []
    try:
        for line in filename:
            number_list.append(int(line.strip()))
        filename.close()
    except IOError:
        print('An error occurred trying to read the file.')
    except ValueError:
        print('Non-integer value found in the file.')
    else:
        print('File read successfully.')
        print('Numbers in the file:', number_list)
        print('Sum of numbers:', sum(number_list))
        print('Average of numbers:', sum(number_list) / len(number_list))

if __name__ == '__main__':
    main()
