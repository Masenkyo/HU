leeftijd = input('geef je leeftijd: ')
leeftijd = int(leeftijd)
paspoort = input('heb je een nederlands paspoort? (y/n?): ')
if leeftijd >= 18 and paspoort == 'y':
    print('gefeliciteerd, je mag stemmen!')
else:
    print('je mag niet stemmen!')