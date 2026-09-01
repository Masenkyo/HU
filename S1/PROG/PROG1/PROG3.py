from shlex import join

a = 6
b = 7
c = (a+b)/2

voornaam = 'Sil'
achternaam = 'Wever'
mijnNaam = voornaam,achternaam

print('PROG3')
print(c)
print(join(mijnNaam))