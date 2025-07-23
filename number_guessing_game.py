from random import randint

lower_num, higher_num = 1, 10
random_num = randint(lower_num, higher_num)

print(f"guess the number in range of {lower_num} to {higher_num}")

while True:
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print(f"Please use only numbers ex: 1")
        continue
    
    if user_guess > random_num:
        print('The number is lower')
    elif user_guess < random_num:
        print('The number is higher')
    else:
        print('Correct!!! you win')
        break

