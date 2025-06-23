"""
This module creates new entries into the roster.
"""

# Valid positions
positions = ['QB', 'HB', 'WR', 'TE', 'LT', 'LG', 'C', 'RG', 'RT', 
             'LE', 'DT', 'RE', 'LOLB', 'MLB', 'ROLB', 'CB', 'FS', 'SS',
             'K', 'P']

def create(roster):
    # roster is a dictionary
    name = input("Enter player's name: ").title()
    position = input("Enter player's position: ").upper()

    # Input validation
    while position not in positions:
        position = input(f"Invalid input. Position must be one of the following:\n{positions}\nEnter player's position: ").upper()
    
    roster[name] = position

    return roster
