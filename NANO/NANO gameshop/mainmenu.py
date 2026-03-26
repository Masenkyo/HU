import json
import hashlib
from os import path
from guesser import GuessNumber
from galgje import Choose
from weather import WeatherGuesser

jsonFile = 'accountInfo.json'

def getHash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def loadData(jsonFile):
    if path.exists(jsonFile):
        with open(jsonFile, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def CreateAccount():
    data = loadData(jsonFile)
    name = input('enter username: ')

    if name in data:
        print('username already in use!')
        return AccountMenu()

    password = input('enter password: ')
    data[name] = getHash(password)

    with open(jsonFile, 'w') as file:
        json.dump(data, file, indent=4)

    print('account has been created!')
    return AccountMenu()

def LogIn():
    data = loadData(jsonFile)
    name = input('enter username: ')
    password = input('enter password: ')

    if name in data and data[name] == getHash(password):
        print(f'Welcome {name}!')
        return Menu()

    print('wrong username or password')
    return AccountMenu()

def AccountMenu():
    choice = input("1. log in, 2. maak account aan")
    match choice:
        case '1':
            return LogIn()
        case '2':
            return CreateAccount()

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

if __name__ == '__main__':
    AccountMenu()