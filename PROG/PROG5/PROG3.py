from gettext import find


def naamBoeitNiet():
    textFile = open('oefening_5_2_kaartnummers.txt', 'r').read().replace('\n', ', ').split(', ')
    numbers = []
    for i in textFile:
        if i.isdigit():
            numbers.append(i)
    print(max(numbers))

naamBoeitNiet()