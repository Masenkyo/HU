firstWord = 'Supercalifragilisticexpialidocious'
secondWord = 'Antidisestablishmentarianism'
thirdWord = 'Honorificabilitudinitatibus'
words = 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'

print('PROG2')
print(f'1. {len(firstWord)}')
print(f'2. {firstWord.find('ice')!=1}')
print(f'3. {len(secondWord) > len(thirdWord)}')
print(f'4. The first word is {sorted(words)[0]} and the last word is {sorted(words)[6]} in alphabetic order.')