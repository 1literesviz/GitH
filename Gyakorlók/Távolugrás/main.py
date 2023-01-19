from functions import menu,fajlBetoltes,versenyzoKiir,eredmenyKiir,ujEredmeny
from os import system

fajlBetoltes()

valasztas=''
while valasztas!='0':
    valasztas=menu()
    if valasztas=='1':
        versenyzoKiir()
    elif valasztas=='2':
        system('cls')
        print('-------EREDMÉNYEK--------')
        eredmenyKiir()
        input()
    elif valasztas=='3':
        ujEredmeny()
    elif valasztas=='4':
        pass