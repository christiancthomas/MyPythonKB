def main():
    with open("source/fundamental/exam_2_review/random_numbers.txt", "r") as infile:
        try:
            for line in infile:
                print(f"{line.rstrip()}")
        except IOError:
            print("IOError occurred.")

main()