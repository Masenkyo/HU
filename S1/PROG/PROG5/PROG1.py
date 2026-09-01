def gemiddelde(woorden):
    lst = woorden.split(' ')
    lengths = 0
    for word in lst:
        lengths += len(word)
    return lengths / len(lst)

print(round(gemiddelde('ik volg de les nu maar half en maak deze opdracht zodat ik hem later niet hoef te maken'), 2))