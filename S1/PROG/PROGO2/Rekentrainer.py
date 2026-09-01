import random

txtFile = 'rekenen.txt'

def main():
    keuze = input("1. RekenSessie\n2. FoutRapport\n3. Reset\n")
    match keuze:
        case '1':
            bewerking = input("(+,-,*)\n")
            aantal = input("aantal sommen: ")

            match input("easy/hard: "):
                case "easy":
                    min, max = 0, 10
                case "hard":
                    min, max = -10, 100
                case _:
                    return

            rekenSessie(bewerking, aantal, min, max)
            main()
        case '2':
            for fout in foutRapport():
                print(fout)
            main()
        case '3':
            reset()
        case _:
            quit()


def rekenSessie(bewerking, aantal, min, max):
    goedCount = 0
    with open(txtFile, 'a') as reken:
        for i in range(int(aantal)):
            first = random.randint(min, max)
            second = random.randint(min, max)

            match bewerking:
                case "+":
                    correctAntwoord = first + second
                case "-":
                    correctAntwoord = first - second
                case "*":
                    correctAntwoord = first * second
            try:
                gegevenAntwoord = int(input(f'wat is {first} {bewerking} {second}: '))
            except:
                ValueError()
            if gegevenAntwoord == correctAntwoord:
                status = 'goed'
                goedCount += 1
            else:
                status = 'fout'
            reken.write(f'{first};{bewerking};{second};{correctAntwoord};{gegevenAntwoord};{status}\n')
    return print(f'je hebt er {goedCount} van de {int(aantal)} goed!')

def foutRapport():
    result = []
    with open(txtFile, 'r') as reken:
        for line in reken.readlines():
            fout = line.strip('\n').split(';')
            if fout[5] == 'goed':
                continue

            result.append(f'{fout[0]} {fout[1]} {fout[2]} is helaas geen {fout[4]}')
    return result

def reset():
    with open(txtFile, 'w') as reken:
        reken.close()
    return main()


if __name__ == '__main__':
    main()