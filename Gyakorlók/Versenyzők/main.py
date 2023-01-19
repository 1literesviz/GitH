from functions import*
FajlBeolvasas()
print(f"3.feladat: Versenyzők száma: {len(versenyzok)}")
print(f"4. feladat: A női versenyzők aánya: {Noiversenyzok():.2f}%")
print(versenyzok[39].Osszpont())
print('6.Feladat : A Bajnok női versenyő')
print(f'\t Név: {versenyzok[noibajnok()].Nev}')
print(f'\t Név: {versenyzok[noibajnok()].Egyesulet}')
print(f'\t Név: {versenyzok[noibajnok()].Osszpont()}')

ferfipontok()
print('8.feladat: Egyesület')
statisztika()