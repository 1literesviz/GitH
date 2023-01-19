from errno import ESTALE
from re import I
from unicodedata import name


names = ['BASTIEN Steven', 'dos SANTOS Felipe', 'DUBLER Cedric', 'ERM Johannes', 'HELCELET Adam Sebastian', 
         'KAZMIREK Kai', 'LEPAGE Pierce', 'MAYER Kevin', 'MOLONEY Ashley', 'ROE Martin', 'SCANTLING Garrett', 
         'SHKURENYOV Ilya', 'SYKORA Jiri', 'TILGA Karel', 'UIBO Maicel', 'URENA Jorge', 'VICTOR Lindon', 
         'WARNER Damian', 'WIESIOLEK Pawel', 'ZHUK Vitaliy', 'ZIEMEK Zachery' ]
points = [8236, 7880, 7008, 8213, 8004, 8126, 8604, 8726, 8649, 7863, 8611, 8413, 7943, 7018, 8037,
          8322, 8414, 9018, 8176, 8131, 8435] 

# A 2021-es olimpián tízpróbában a names listában felsorolt versenyzők indultak. Elért eredményeiket a points lista tartalmazza.
# Oldja meg az alábbi feladatokat!

# Írja ki a képernyőre, hogy a 2021-es olimpián hány atléta teljesített a 10 próbát!
print(f'A versenyen {len(names)} versenyző indult.')

# Írja ki a képernyőre, hány olyan versenyző volt, aki legalább 8600 pontot ért el!
db=0
for item in points:
    if item >= 8600:
        db+=1
print(f'{db} versenyző ért el legalább 8600 pontot.')


# Írja ki a képernyőre a versenyzők pontszámának az átlagát!
osszeg = 0
for item in points:
    osszeg+=item
print(f'A versenyzők által elért pontszámok átlaga: {osszeg/len(names):.2f}')

# Írja ki a képrnyőre a győztes versenyző nevét és pontszámát!
maxpos=0
for item in range(1,len(points)):
    if points[items]>points[maxpos]:
        maxpos=item
print(f"A verseny győztese : {names[maxpos]} {points[maxpos]} pontos eredménnyel.")


# Kérje be a felhasználótól egy versenyző nevét és írja ki pontszámát!

# Ha nem találja, írja ki, hogy a versenyző nem indult a versenyen

bekernev=input("Versenyző neve: ")
i=0
while i<len(names) and names [i]!=bekernev:
    i+1
if i<len(names):
    print(f'\tA versenyző pontszáma: {points[i]}')
else:
    print('\tA versenyző neve nem szerepel a listán')
