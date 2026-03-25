from guesser import GuessNumber
from galgje import Choose
from weather import WeatherGuesser

def Menu():
    game = input("kies je game (1. guesser, 2. galgje, 3. weatherguesser): ")
    match game:
        case '1':
            GuessNumber()
        case '2':
            Choose()
        case '3':
            WeatherGuesser()
        case _:
            print("tot volgende keer!")

Menu()