def main():
    sum = 0
    with open("source/fundamental/exam_2_review/random_numbers.txt", "r") as infile:
        try:
            for line in infile:
                sum += int(line)
            avg = sum / int(line)
            print(f"Avg: {avg:.2f}")
        except IOError:
            print("IOError occurred.")

main()