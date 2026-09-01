from shlex import join
from PROG3 import a, b, c, mijnNaam, voornaam, achternaam

print('PROG4')
print(f'1. 6.75 is groter dan a {6.75>a} en kleiner dan b {6.75<b}')
print(f'2. mijnNaam is even groot als de lengtes van voornaam, tussenvoegsel en achternaam = '
      f'{len(join(mijnNaam)) == len(voornaam+achternaam)} want er zijn spaties toegevoegt.')
print(f'3. is de lengte van mijnNaam minstens 5 keer zo groot als variable c? {len(join(mijnNaam)) > c*5}')
print(f'4. ik heb geen tussenvoegsel maar als ik wel 1 had zou ik dit doen (tussenvoegsel in achternaam)')