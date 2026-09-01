cijferPROJA = 9
cijferPROG = 10
cijferMOD = 8

# def Average(a, b, c):
#     return (a + b + c) / 3


# i used this instead because now you can do a infinite amount of variables and it would still work, the previous one only enabled me to do 3 variables at a time.
def Average(*average):
    addedTotal = sum(average)
    amountNumbers = len(average)
    return addedTotal / amountNumbers

print(Average(cijferPROJA, cijferPROG, cijferMOD))
print()