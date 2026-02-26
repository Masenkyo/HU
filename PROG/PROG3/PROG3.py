maandNummer = input('kies een maand: ')
maandNummer = int(maandNummer)
if maandNummer >= 3 and maandNummer <= 5:
    print('lente')
elif maandNummer >= 6 and maandNummer <= 8:
    print('zomer')
elif maandNummer >= 9 and maandNummer <= 11:
    print('herfst')
elif maandNummer > 12 or maandNummer < 1:
    print('ongeldige input')
else:
    print('winter')