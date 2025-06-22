import random

numbers = [0, 0, 0, 0, 0, 0, 0]
for i in range(len(numbers)):
    numbers[i] = random.randrange(0,10)
for num in range(len(numbers)):
    print(f"Lottery #{num + 1} is: {numbers[num]}")