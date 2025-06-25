"""
This program creates a pet object and sets its attributes.
"""

from pet import Pet

def main():
    # Create a Pet object
    pet = Pet()

    name = input("Enter the pet's name: ")
    animal_type = input("Enter the pet's type: ")
    age = input("Enter the pet's age: ")

    # Set the pet's attributes
    pet.set_name(name)
    pet.set_animal_type(animal_type)
    pet.set_age(age)

    # Display the pet's information
    print(f"\n{pet.get_name()} is a {pet.get_animal_type()} and is {pet.get_age()} years old.\n")

if __name__ == "__main__":
    main()