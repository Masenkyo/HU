def woordInput(woord = ''):
    while len(woord) < 4:
        woord = input('typ een woord van minimaal 4 letters: ')
    return f'{woord} heeft {len(woord)} letters!'
print(woordInput())