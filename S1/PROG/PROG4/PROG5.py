def kwadraten_som(grondgetallen = []):
    totaal = 0
    for getallen in grondgetallen:
        if getallen > 0:
            totaal += getallen
    return totaal

print(kwadraten_som([1, 10 ,14, -14, -34, 22]))