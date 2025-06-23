"""
This module reads existing roster entries.
"""

def read(roster):
    player = input("Enter player's name or \"all\" to view entire roster: ").title()
    # look up player on roster
    if player == "All":
        print(f"Player: Position\n-------------------")
        for row in roster:
            print(f"{row}: {roster[row]}")
    else: 
        print(f"{player}: {roster.get(player, 'Not found')}")