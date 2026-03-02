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


# still need to fix decimals being .00000000003 and .245 need to round up from 5 otherwise down and make console better to look at.
def testBezorgFuncties():
    types = 'normaal', 'zakelijk', 'spoedig'
    distances = -5, -4, 0, 4, 5, 10, 11, 30, 31
    spoedig = True, False
    for klantType in types:
        print('klantType =', klantType)
        for afstandKM in distances:
            print('afstandKM =', afstandKM)
            for spoed in spoedig:
                print('spoedig =', spoed)
                print(definitieveBezorgkosten(klantType, spoed, afstandKM))

testBezorgFuncties()


print(definitieveBezorgkosten('normaal', True, 24))