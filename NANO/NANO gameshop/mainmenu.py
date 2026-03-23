from guesser import GuessNumber
from galgje import Choose

def Menu():
    game = input("kies je game (1. guesser, 2. galgje): ")
    match game:
        case '1':
            GuessNumber()
        case '2':
            Choose()
        case _:
            print("tot volgende keer!")

Menu()