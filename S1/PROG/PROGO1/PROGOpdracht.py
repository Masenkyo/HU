#region basisBezorgkostenComments
# def basisBezorgkosten(afstandKM):
#     basisKost = 4.50
#     if afstandKM > 10 and afstandKM <= 30:
#         return basisKost + (afstandKM - 10) * 0.25
#     elif afstandKM > 30:
#         return -1
#     else:
#         return basisKost
# ik wou kijken of ik alles hierboven in 1 return line kon doen en het kan! Check hierboven voor overzichtelijkere versie.
# ik heb ternary gebruikt om het op 1 return lijn te krijgen. ook koos ik ervoor om als hij onder de 10 is met else te doen,
# want met min getallen moeten we gewoon doen alsof het 0 is en else valt daar ook onder.
# minimal effort but maximum performance.
#regionend
def basisBezorgkosten(afstandKM):
    return 4.50 + (afstandKM - 10) * 0.25 if afstandKM > 10 and afstandKM <= 30 else -1 if afstandKM > 30 else 4.50

#region definitieveBezorgkosten comments
# checken voor -1 en dan checken voor gevraagde dingen in opdracht zoals korting voor zakelijk als het 5 of meer km ervan vandaan is.
# korting door * 0.8 of 0.9 te doen en spoed toeslag toevoegen bij normale klanten en anders gewoon normale prijs.
#endregion
def definitieveBezorgkosten(klantType, spoed, afstandKM):
    basisKost = basisBezorgkosten(afstandKM)
    if basisKost == -1:
        return -1

    if klantType == 'zakelijk' and afstandKM >= 5:
        return basisKost * 0.9
    elif klantType == 'spoedig':
        return basisKost * 0.8
    elif klantType == 'normaal' and spoed:
        return basisKost + 3
    else: return basisKost

#region testBezorgFunctiesOld functie + info over nieuwe functie
# het probleem met deze versie is dat ik 0.0000000000003 kreeg op sommige en dat de console cluttered en lelijk was.
# def testBezorgFuncties():
#     types = 'normaal', 'zakelijk', 'spoedig'
#     distances = -5, -4, 0, 4, 5, 10, 11, 30, 31
#     spoedig = True, False
#     for klantType in types:
#         print('klantType =', klantType)
#         for spoed in spoedig:
#             print('spoedig =', spoed)
#             for afstandKM in distances:
#                 print('afstandKM =', afstandKM)
#                 print(definitieveBezorgkosten(klantType, spoed, afstandKM))
# adding rounding up and better console readability using formula i found somewhere and adding :.2f at the end for letting them end on 2 decimals.
# also using :< and :> to add spaces to the prints so i can read console normally without making my eyes hurt... idk why i wrote this part in english but idc...
#endregion
def testBezorgFuncties():
    print(f'klantType | spoed | afstandKM | prijs')
    print('-' * 40)
    for klantType in 'normaal', 'zakelijk', 'spoedig':
        for spoed in (False, True):
            for afstandKM in -5, -4, 0, 4, 5, 10, 11, 30, 31:
                display = f'{int(definitieveBezorgkosten(klantType, spoed, afstandKM) * 100 + 0.5) / 100.0:.2f}'
                print(f"{klantType:<9} | {str(spoed):<5} | {afstandKM:>7}km | {display:>5}")

testBezorgFuncties()