import requests

def info():
    key = "aef970e5de15ffde15625b1971172283"

    while True:
        try:
            userCity = input("Enter a city to get the weather: ")


            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={userCity}&appid={key}&units=metric")
            data = response.json()

            valueMain = data["main"]
            break
        except Exception:
            print('try again, you probably misspelled it...')
    temperature = int(valueMain["temp"])
    return temperature

def WeatherGuesser():
    temperature = info()
    guess = -100
    while guess != temperature:
        try:
            guess = int(input('Guess temperature: '))
        except Exception:
            print('enter a number')
            continue

        isItNear = abs(guess - temperature)

        if guess == temperature:
            break

        if isItNear <= 1:
            print('near')
        elif guess > temperature:
            print('lower')
        else:
            print('higher')

    print('you won gg!')

if __name__ == '__main__':
    WeatherGuesser()