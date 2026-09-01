import json
from os import path

jsonFile = 'overheidInfo.json'

while True:
    naam = input("Wat is je achternaam? ")
    if naam == '':
        break

    voorletters = input("Wat zijn je voorletters? ")
    geboortedatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")

    info = {
        "naam": naam,
        "voorletters": voorletters,
        "geb_datum": geboortedatum,
        "e-mail": email
    }

    if path.exists(jsonFile):
        with open(jsonFile, 'r') as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    data = [data] if data else []
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(info)

    with open(jsonFile, 'w') as file:
        json.dump(data, file, indent=4)