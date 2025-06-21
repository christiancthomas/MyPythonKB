import random

def main():
    filename = "source/fundamental/exam_2_review/random_numbers.txt"
    outfile = open(filename, "w")
    num = int(input("How many numbers to write? "))
    max_val = int(input("Top of number range? "))

    for _ in range(num):
        val = random.randint(1, max_val)
        outfile.write(f"{val}\n")
    outfile.close()

main()
