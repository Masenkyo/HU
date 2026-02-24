import random

def Score(difficulty, attempts, maxAttempts):
    return (maxAttempts - attempts) * difficulty

def DifficultyAdvice(score, difficulty, maxAttempts, won):
    if not won:
        return 'try something easier' if difficulty > 1 else 'try again'

    performance = score / (difficulty * maxAttempts)

    if performance >= 0.8:
        return 'try something harder' if difficulty < 3 else 'you have conquered the highest level possible, good job..'
    if performance >= 0.4:
        return 'stay on this lvl :p'
    else:
        return 'try something easier' if difficulty > 1 else 'lock in :['


def GuessNumber():
    guessRange = 10, 50, 100
    attemptRange = 5, 7, 10
    won = False

    naam = input('Enter your name: ')
    print(f'thank you for choosing the number guessing game {naam}')

    while True:
        difficulty = input('choose difficulty: 1 easy, 2 medium, 3 hard')
        try:
            difficulty = int(difficulty)
            if difficulty not in [1, 2, 3]:
                print('please choose difficulty: 1 easy, 2 medium, 3 hard')
                continue
            break
        except ValueError:
            print('invalid input, choose a number between 1 and 3')

    currentGuessRange = guessRange[difficulty - 1]
    randomNumber = random.randint(1, currentGuessRange)
    maxAttempts = attemptRange[difficulty - 1]
    attempts = 0

    while attempts < maxAttempts:
        print(f'{maxAttempts - attempts} remaining attempts and current score is {Score(difficulty, attempts, maxAttempts)}')
        guessInput = input(f'guess a number between 1 and {currentGuessRange}: ')
        try:
            guess = int(guessInput)
            if not (1 <= guess <= currentGuessRange):
                print(f'Please enter a number between 1 and {currentGuessRange}')
                continue
        except ValueError:
            print("a number... stoopid")
            continue

        attempts += 1

        if guess == randomNumber:
            won = True
            break
        else:
            isItNear = abs(guess - randomNumber)
            if isItNear <= difficulty:
                print('you are near the random number')
            elif guess > randomNumber:
                print('lower')
            else:
                print('higher')

    if won:
        print('you guessed the hidden number!!!')
    else:
        print('you lost lol bwuhaahwah')

    print(DifficultyAdvice(Score(difficulty, attempts, maxAttempts), difficulty, maxAttempts, won))

    again = input('do you want to play again? (y/n)')
    if again == 'y':
        GuessNumber()
    else:
        print('ok bye')

if __name__ == '__main__':
    GuessNumber()