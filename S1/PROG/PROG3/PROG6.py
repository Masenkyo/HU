s = "Guido van Rossum heeft programmeertaal Python bedacht."
aeiou = 'aeiou'
for klinkers in s:
    for letters in aeiou:
        if klinkers == letters:
            print(klinkers)
