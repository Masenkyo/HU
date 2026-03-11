def summing(guess):
    while guess[-1] != 0:
        guess.append(int(input('Choose a number: ')))
    return [sum(guess) - 1]

print(summing([1]))