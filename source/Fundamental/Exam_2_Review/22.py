def main():
    with open("source/fundamental/exam_2_review/random_numbers.txt", "r") as infile:
        try:
            line = infile.readline()
            while line != "":
                print(f"{line.rstrip()}\n")
                line = infile.readline()
        except IOError:
            print("IOError occurred.")

main()