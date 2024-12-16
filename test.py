import random

def game():
    choices = ['r', 'p', 's']  # r for rock, p for paper, s for scissors
    random_pick = random.choice(choices)
    guess = ''

    while guess != random_pick:
        guess = input('What is your guess? (r for rock, p for paper, s for scissors): ').lower()
        if guess not in choices:
            print('Invalid input. Please choose r, p, or s.')
            continue

        print(f'Computer chose: {random_pick}')

        if guess == random_pick:
            print('It\'s a tie!')
        elif (guess == 'r' and random_pick == 's') or (guess == 'p' and random_pick == 'r') or (guess == 's' and random_pick == 'p'):
            print('You win!')
        else:
            print('You lose!')

        random_pick = random.choice(choices)

# Call the game function to play
game()
