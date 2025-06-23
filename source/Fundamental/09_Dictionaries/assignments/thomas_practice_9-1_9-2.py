"""
Christian Thomas
Complete 

This program is a roster management tool for a fictional football team: The ACC Riverbats 🦇

The roster will be held in a dictionary with key-value pairing as: Full Name: Position
It will operate similarly to a CRUD endpoint, with options to create new entries,
read info on existing players, update existing data, and delete entries. Each CRUD
function will exist in a separate module and will be imported into main which will hold
the main program and menu functionality.
"""

import create, read, update, delete
import pickle

# Global constants for menu choices
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
QUIT = 5

def main():
    # initializations
    roster = {}
    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        # load pickled dict
        load(roster)

        if choice == CREATE:
            create.create(roster)
        elif choice == READ:
            read.read(roster)
        elif choice == UPDATE:
            update.update(roster)
        elif choice == DELETE:
            delete.delete(roster)
        
        # save pickled dict
        save(roster)
    """
    TODO:
    - Save the dictionary – write a function to pickle the dictionary to a file
    - Retrieve the dictionary – write a function to retrieve the pickled
    dictionary that was saved earlier
    - Put both functions in a separate module that is imported by your main
    program
    """

# Get menu choice from user
def get_menu_choice():
    print()
    print('ACC Riverbat Roster Tool 🦇')
    print('---------------------------')
    print('1. Add a new player')
    print('2. View an existing player')
    print('3. Update an existing player')
    print('4. Delete a player')
    print('5. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Choose an option: '))

    # Validate the choice.
    while choice < CREATE or choice > QUIT:
        choice = int(input('Enter a valid choice (1-5): '))

    return choice


if __name__ == "__main__":
    main()
