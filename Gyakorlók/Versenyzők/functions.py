from data import *

def FajlBeolvasas():
    f=open('fob2016.txt','r', encoding='utf8')
    for sor in f:
        versenyzok.append(versenyzo(sor))
    f.close()

# def Noiversenyzok():
#     noidb=0
#     for item in versenyzok:
#         if item.Kategoria == 'Noi':
#             noidb+=1
#     return noidb

def Noiversenyzok():
    noiDb=0
    for item in versenyzok:
        if item.Kategoria=="Noi":
            noiDb+=1
    return noiDb/len(versenyzok)*100

def noibajnok():
    bajnokPoz=0
    for i in range(len(versenyzok)):
        if versenyzok[i].Kategoria == 'Noi' and versenyzok[i].Osszpont()>versenyzok[bajnokPoz].Osszpont():
            bajnokPoz=i
    return bajnokPoz

def ferfipontok():
    f=open('osszpontFF.txt','w',encoding='utf-8')
    for item in versenyzok:
        if item.Kategoria == 'Felnott ferfi':
            f.write(f'{item.Nev};{item.Osszpont()}\n')
    f.close()

def statisztika():
    stat={}
    for item in versenyzok:
        if item.Egyesulet!='n.a':
            if item.Egyesulet in stat.keys():
                stat[item.Egyesulet]+=1
            else:
                stat[item.Egyesulet]=1

    for key, value in stat.items():
        if value>2:
            print(f'{key} - {value}')

    f=open('statisztika.txt' , 'w' , encoding='utf-8')
    for key, value in stat.items():
        if value>2:
            f.write(f'{key} - {value}\n')
    f.close()

