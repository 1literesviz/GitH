class versenyzo:
    #Albert Laszlo;Felnott ferfi;HOLE HUNTERS;0;0;10;10;0;0;0;10
    def __init__(self,sor:str):
        adatok=sor.strip().split(';')
        self.Nev=adatok[0]
        self.Kategoria=adatok[1]
        self.Egyesulet=adatok[2]
        self.Pontszamok=[]
        for i in range(3,len(adatok)):
            self.Pontszamok.append(int(adatok[i]))



    def Osszpont(self):
        pontok=self.Pontszamok
        pontok.sort()
        ossz = sum(pontok)
        if pontok[0]!=0:
            ossz=ossz-pontok[0]+10
        if pontok[1]!=0:
            ossz=ossz-pontok[1]+10
        return ossz
versenyzok:list[versenyzo]=[]