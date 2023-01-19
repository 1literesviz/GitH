from data import nevek,ugrasok
from os import system
fajlnev='jumps.csv'

def menu():
    system('cls')
    print('----------MENÜ----------')
    print('0 - Kilépés')
    print('1 - Versenyzők')
    print('2 - Eredmények')
    print('3 - Új eredmény felvétele')
    print('4 - Eredmény törlése')
    return input('Választás: ')

def fajlBetoltes():
    file=open(fajlnev,'r',encoding='utf-8')
    for sor in file:
        #sor-->'Kovács Béla;7.56\n'
        darabolt=sor.strip().split(';')
        nevek.append(darabolt[0])
        ugrasok.append(float(darabolt[1]))        
    file.close()
    
def versenyzoKiir():
    system('cls')
    print('-------VERSENYZŐK--------')
    for nev in nevek:
        print(f'\t{nev}')
    input()

def eredmenyKiir():
    for i in range(len(nevek)):
        print(f'\t{i+1}. {nevek[i]}: {ugrasok[i]}')

def ujEredmeny():
    system('cls')
    print('------ÚJ EREDMÉNY--------')
    bekertNev=input('Név: ')
    bekertUgras=float(input('Ugrás: ').replace(',','.')) #megadhatjuk ,-vel is
    nevek.append(bekertNev)
    ugrasok.append(bekertUgras)
    eredmenyMentesFajlVegere(bekertNev,bekertUgras)
    input('Sikere felvétel.')

def eredmenyMentesFajlVegere(nev,ugras):
    file=open(fajlnev,'a',encoding='utf-8')
    file.write(f'\n{nev};{ugras}')
    file.close()