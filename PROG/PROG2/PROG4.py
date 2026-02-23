from random import randint

muntStukken = [50, 20, 10, 5, 2, 1]
geld = int(input('hoeveel geld neem je mee: '))
prijs = randint(10, 150)
overigeGeld = geld - prijs
muntenLijst = []

print('het product is', str(prijs))
print('je houd zoveel geld over', overigeGeld)
for munten in muntStukken:
    overig = overigeGeld % munten
    hoevaakMunt = overigeGeld // int(munten)
    muntenLijst.append(hoevaakMunt)
    overigeGeld = overig

print(muntenLijst)

