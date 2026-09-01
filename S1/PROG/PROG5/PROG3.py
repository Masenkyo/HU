def naamBoeitNiet():
    textFile = open('oefening_5_2_kaartnummers.txt', 'r').readlines()
    biggestNumber = 0
    whatLine = 0

    # de i is de lijnen en line is wat er in de lijn zelf staat. en enumerate geeft mij dus de nummer en de context van die line.
    # die nummer in enumerate zegt basicly dat hij niet bij 0 moet beginnen met tellen, maar bij 1. anders zegt hij lijn 3 ofzo.
    # en bij de line.split zeg ik gewoon dat hij naar de nummer moet kijken, ik split namelijk bij de , dus het eerste is de nummer en dan de tweede de rest dat na de comma zat.
    # bij de if statement check ik gewoon of hij groter was dan eerst en dan bruteforce ik eigenlijk de grootste nummer zo xD.
    for i, line in enumerate(textFile, 1):
        number = int(line.split(',')[0])
        if number > biggestNumber:
            biggestNumber = number
            whatLine = i

    print(f"Deze file telt {len(textFile)} regels")
    print(f"Het grootste kaartnummer is: {biggestNumber} en dat staat op regel {whatLine}")

naamBoeitNiet()