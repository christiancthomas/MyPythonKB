"""
This module deletes existing roster entries.
"""

def delete(roster):
    player = input("Player to remove from roster: ").title()
    if player in roster:
        del roster[player]
        print(f"{player} removed from roster.")