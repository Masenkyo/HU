lijst = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
attempts = 0
zoekItem = int(input('kies getal tussen 1/10: '))

for item in lijst:
    attempts += 1
    if item == zoekItem:
        break

print(f'amount of attempts are {attempts}')