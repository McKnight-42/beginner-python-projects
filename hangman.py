from random import choice

def run_game():
    word = choice([
        "Archivist", "Statement", "The Institute", "The Eye", "The Web", "The Flesh", "The Spiral", "The Vast",
        "The Slaughter", "The Buried", "The Stranger", "The Dark", "The Corruption", "The Desolation",
        "The Lonely", "The End", "Fear", "Watcher", "Distortion", "NotThem", "Beholding", "Avatars", 
        "Artifacts", "The Unknowing", "The Extinction", "The Hunt", "Gertrude", "Jon", "Martin", "Elias", 
        "Sasha", "Tim", "Basira", "Daisy", "Michael", "Peter Lukas", "The Coffin", "The Panopticon", 
        "The Tapes", "The Eye Opens", "Paranormal", "Supernatural", "Entity", "Fear God", "Dream Logic", 
        "Power", "Statement Taker", "Web of Lies", "The Angler Fish", "Fear Feeds", "Jane Prentiss", "Worms", 
        "Hive", "The Bone Turner's Tale", "The Library", "Sins of the Father", "The Table", "The Circus", 
        "The End Times", "Apocalypse", "Fear Avatar", "Ritual", "Patron Entity"
    ])

    word_lower = word.lower()
    user_name = input("Please state your name: ")
    print(f"\n---\nStatement of {user_name}, regarding an encounter with... something.")
    print("Statement begins.\n")
    print("Note: Statements may contain multiple words, capital letters, or punctuation.")
    print("Only letters are to be recorded. Non-alphabetic symbols will reveal themselves.\n")

    guessed = ''
    tries = 5

    while tries > 0:
        blanks = 0
        print('Transcript: ', end='')

        for char in word:
            if not char.isalpha():
                print(char, end='')  # Reveal spaces/punctuation
            elif char.lower() in guessed:
                print(char, end='')  # Preserve original casing
            else:
                print('_', end='')
                blanks += 1
        print()

        if blanks == 0:
            print('\nThe Eye is satisfied. The statement is complete.')
            break

        guess = input('Record a letter: ').lower()

        if not guess.isalpha() or len(guess) != 1:
            print("That... doesn't belong in the archive. Only letters, please.")
            continue

        if guess in guessed:
            print(f'You’ve already documented "{guess.upper()}". Or have you?')
            continue

        guessed += guess

        if guess not in word_lower:
            tries -= 1
            print(f'That thread leads nowhere. The Web shifts. Remaining clarity: {tries}')
        else:
            print(f'"{guess.upper()}"... noted.')

        if tries == 0:
            print(f"\nThe statement fades. Unfinished. The truth slips away into the dark.")
            print(f"The phrase was: {word}")
            print("Statement ends.")
            break

if __name__ == '__main__':
    run_game()
