from datetime import datetime

while True:
    naam = input('naam van hardloper: ')

    if not naam:
        break

    nu = datetime.now()
    datum = nu.strftime('%a %d %b %Y, %H:%M:%S')

    # wow check deze site https://www.geeksforgeeks.org/python/with-statement-in-python/, ik ga dit gebruiken, heb alleen niet gebruikt in PROG3 terwijl het wel had gekunt :[
    # ben er net pas achter gekomen :[
    with open('oefening_5_4_hardlopers.txt', 'a') as file:
        file.write(f'{datum}, {naam}\n')