"""
This is a python script that uses functions as steps to make a sandwich. Specifically,
peanut butter and jelly sandwich. The script defines functions for each step of the process,
and then calls these functions in sequence to complete the sandwich-making process.
"""

def step1():
    # gather ingredients and tools
    print("Step 1: Gather the following ingredients and tools:")
    print("- Plate")
    print("- Bread (2 slices)")
    print("- Peanut butter")
    print("- Jelly")
    print("- Butter knife")
    print("- Spoon (optional for jelly)")

def step2():
    # place bread on a plate
    print("Step 2: Place two slices of bread on a plate, side by side.")

def step3():
    # spread peanut butter on one slice of bread
    print("Step 3: Take one slice of bread and spread peanut butter on it using a butter knife.")

def step4():
    # spread jelly on the other slice of bread
    print("Step 4: Take the other slice of bread and spread jelly on it using a butter knife or spoon.")

def step5():
    # combine the two slices
    print("Step 4: Place the slice with peanut butter on top of the slice with jelly to form a sandwich. Enjoy! 🥪")


def main():
    print("This is how to make a peanut butter and jelly sandwich:")
    step1()
    step2()
    step3()
    step4()
    step5()

if __name__ == "__main__":
    main()