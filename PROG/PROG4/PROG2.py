def som(getallenLijst = []):
    totaal = 0
    for getallen in getallenLijst:
        totaal += getallen
    return totaal

print(som([1, 4, 7, 22]))