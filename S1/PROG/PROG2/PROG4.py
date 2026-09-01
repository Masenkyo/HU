from random import randint

muntStukken = [50, 20, 10, 5, 2, 1]
prijs = randint(10, 150)
muntenLijst = []
print('het product is', str(prijs))

while True:
    try:
        geld = int(input('hoeveel geld neem je mee: '))
        if geld < prijs:
            print('bring more money, you too poor rn')
        else:
            break
    except ValueError:
        print('please enter a number')

overigeGeld = geld - prijs
print('je houd zoveel geld over', overigeGeld)
for munten in muntStukken:
    overig = overigeGeld % munten
    hoevaakMunt = overigeGeld // int(munten)
    muntenLijst.append(hoevaakMunt)
    overigeGeld = overig

print(muntenLijst)

