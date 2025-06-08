"""
Christian Thomas
Complete
This program takes as input the number of servings desired and calculates the
ingredients needed for a sauce recipe based on that number of servings.
"""

def inputs():
    servings = int(input("Enter the number of desired servings: "))
    return servings

def process():
    servings = inputs()

    BASE_SAUCE = 2 # cups
    BASE_PASTE = 1/3 # cup
    BASE_GARLIC = 2 # cloves
    BASE_OREGANO = 1 # tablespoon

    sauce = round(BASE_SAUCE * servings / 4, 2)
    paste = round(BASE_PASTE * servings / 4, 2)
    garlic = round(BASE_GARLIC * servings / 4, 2)
    oregano = round(BASE_OREGANO * servings / 4, 2)

    return servings, sauce, paste, garlic, oregano

def outputs(servings, sauce, paste, garlic, oregano):
    print(f"To make {servings} servings, you will need:")
    print(f"{sauce} cups of sauce")
    print(f"{paste} cups of paste")
    print(f"{garlic} cloves of garlic")
    print(f"{oregano} tablespoons of oregano")

if __name__ == "__main__":
    servings, sauce, paste, garlic, oregano = process()
    outputs(servings, sauce, paste, garlic, oregano)

