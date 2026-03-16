import random
def main():
    keuze = int(input("1. RekenSessie\n2. FoutRapport\n3. Reset\n"))
    match keuze:
        case 1:
            bewerking = input("(plus,min,keer)\n")
            aantal = input("aantal sommen: ")

            match input("easy/hard: "):
                case "easy":
                    min, max = 0, 10
                case "hard":
                    min, max = -10, 100
                case _:
                    return

            rekenSessie(bewerking, aantal, min, max)
        case 2:
            foutRapport()
        case 3:
            reset()


def rekenSessie(bewerking, aantal, min, max):
    result = []
    for i in range(int(aantal*2)):
        result.append(random.randint(min, max))

    match bewerking:
        case "plus":
            min + max
        case "min":
            min - max
        case "keer":
            min * max

    return print(result)


def foutRapport():
    return


def reset():
    return


if __name__ == '__main__':
    main()
