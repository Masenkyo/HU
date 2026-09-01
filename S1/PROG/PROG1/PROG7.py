from collections import Counter

letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
# hoeveelheidLetters = Counter(letters) ez fix maar ik denk dat dit niet is wat ik hoor te doen voor deze les

allLetters = sorted(Counter(letters)) # hier gebruik ik alsnog counter maar ik kan ook gewoon a = [A, B, C] doen

# ik heb de list zo gemaakt want ik vond het beter, want anders moet ik .append gebruiken in de loop maar nu word het
# al gelijk toegevoegt aan de nieuwe list variable, anders zag het er zo uit:
# hoeveelheidLetters = []
# for i in allLetters:
#     aantal = letters.count(i)
#     hoeveelheidLetters.append(aantal)
# print(hoeveelheidLetters)
aantallen = [letters.count(i) for i in allLetters]
print(aantallen)