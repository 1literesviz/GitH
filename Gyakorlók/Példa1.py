from data import*

def fajlbeolvasas():
    f=open('orvosi_nobeldijak.txt','r', encoding='utf8')
    f.readline()
    for sor in f:
        nobeldijjasok.append(Nobel(sor))
    f.close()


def utolsóév(a):
    max_év = 0
for nobeldijas in nobeldijjasok:
     if nobeldijjas.Év > max_év:
         max_év = nobeldijjas.Év
         a = nobeldijas.Év

def orszagKod():
    db=0
    be = input("Kérem adja meg az ország kódját!")
    for nobeldijas in nobeldijjasok:
        if nobeldijas.OrszágKód == be_orszag_kod:
            db +=1
            jonobeldijas = nobeldijas
    if db == 0:
        print("A megadott országban nem volt díjjazott")
    elif db > 1:
        print(f"A megadott az országból {db} fő díjazott volt!")
    else:
        print(f'\tA megadott ország díjazottja:')
        print(f'\tNév:{jonobeldijas.Név}')
        print(f'\tÉv{jonobeldijas.Év}')
        print(f'\tSz/h {jonobeldijas.SzületésHalálozás}')