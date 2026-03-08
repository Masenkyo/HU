def Convert(celcius):
    return celcius * 1.8 + 32

def Table():
    result = ''
    print('Fahrenheit | Celsius')
    print('-'*20)
    for graden in range(-30, 41, 10):
        result += f'{Convert(graden):10} | {graden:5.1f}\n'
    return result

print(Table())