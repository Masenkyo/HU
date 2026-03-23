from guesser import GuessNumber
from galgje import Main

game = input("kies je game (1. guesser, 2. galgje): ")
match game:
    case '1':
        GuessNumber()
    case '2':
        Main()
    case _:
        print("tot volgende keer!")