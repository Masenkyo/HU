from json import dump

jsonFile = 'overheidInfo.json'

while True:
    naam = input("Wat is je achternaam? ")
    if naam == '':
        break

    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")

    info = {
        "naam": naam,
        "voorletters": voorl,
        "geb_datum": gbdatum,
        "e-mail": email
    }

    with open(jsonFile, 'a') as f:
        dump(info, f, indent=4)