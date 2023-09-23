import random

game_mode = input('Who will be the guesser?\nMe/computer: ').lower()

if game_mode == 'me':
    def guess(x):
        random_num = random.randint(1, x) 
        guess = 0

        while guess != random_num:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < random_num:
                print('Too low, kid!')
            elif guess > random_num:
                print('Too high, kid!')

        print(f"You Got it !!! Congrats. You've guessed the number {random_num}")

    guess(20)

else:
    def computer_guess(x):
        low = 1
        high = x
        feedback = ''

        while feedback != 'c':
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low  # Ou high, porque low = high
            feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1

        print('YEEEEE!!! I am the best.')

    computer_guess(20)
