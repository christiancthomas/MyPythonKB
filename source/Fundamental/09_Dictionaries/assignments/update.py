"""
This module updates existing entries.
"""

# Valid positions
positions = ['QB', 'HB', 'WR', 'TE', 'LT', 'LG', 'C', 'RG', 'RT',
             'LE', 'DT', 'RE', 'LOLB', 'MLB', 'ROLB', 'CB', 'FS', 'SS',
             'K', 'P']

def update(roster):
    player = input("Which player's position are you updating? ").title()
    if player in roster:
        new_pos = input("Enter new position: ").upper()
        # Input validation
        while new_pos not in positions:
            new_pos = input(f"Invalid input. Position must be one of the following:\n{positions}\nEnter player's position: ").upper()
        # update position
        roster[player] = new_pos
        print(f"{player}'s position has been updated to {new_pos}")
    else:
        print(f"{player} not found on roster.")


