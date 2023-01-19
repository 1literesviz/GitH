from varosok import *

varosoklista = []


def FajlBeolvas():
    file=open('varosok.txt','r', encoding='utf-8')
    file.readline()
    for sor in file:
        waros = varos(sor)
        varosoklista.append(waros)
    file.close()

def indiaiLakosok():
    osszeg = 0
    for item in varosoklista:
        if item.Orszag == 'India':
            osszeg+=item.Lakossag
    return osszeg*1000

def legnagyibbVaros():
    for i in range(len(varosokLista)):
        max=varosoklista[0].Lakossag
        maxPoz = 0
    return maxPoz

def magyarKeres ():
    for item in varosoklista:
        if item.Orszag == 'Magyarország':
            return 'Van magyar város az adatok között'
    return 'Nincsen magyar város az adatok között'

def egyszokoz():
    db = 0
    for item in varosoklista:
        if len(item.Nev.split(' '))== 2:
            db +=1
        return db

def statkeszit():
    stat = {} #dictionary
    for item in varosoklista:
        if item.Orszag in stat.key():
            stat[item.Orszag]+=1
        else:
            stat[item.Orszag]=1
    for key,value in stat.item():
        print(f'\t {key} - {value} db')
