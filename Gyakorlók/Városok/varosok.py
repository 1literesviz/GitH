class varos:
    def  __init__(self,sor):
        adatok=sor.strip().split(';')
        self.Nev=adatok[0]
        self.Orszag = adatok[1] 
        self.Lakossag=int(adatok[2])
        