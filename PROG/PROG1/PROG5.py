favorieten = ['Kanye West']

print(f'1. {favorieten[0]}')

favorieten.append('Adam Levine')
# ik zou dit gebruiken maar dan heb ik geen comma print(*favorieten)
print(f'2. {', '.join(favorieten)}')

favorieten[1] = 'Michael Jackson'
print(f'3. {', '.join(favorieten)}')