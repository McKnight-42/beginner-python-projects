from random import randint
from typing import Tuple

def roll_dice(amount: int = 2) -> Tuple[list[int], int]:
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []

    for _ in range(amount):
        roll: int = randint(1, 6)
        rolls.append(roll)
    
    total = sum(rolls)
    return rolls, total

def main():
    while True:
        try:
            user_input: str = input(f"How many D6's would you like to roll? (Press Enter for 2): ")

            if user_input.lower() == 'exit':
                print(f"Thanks for playing!")
                break

            amount = int(user_input) if user_input else 2  # default to 2
            rolls, total = roll_dice(amount)
            print(f"Rolls: {', '.join(str(r) for r in rolls)} | Total: {total}")
            
        except ValueError:
            print('Please enter a valid number ex. 3')

if __name__ == '__main__':
    main()
