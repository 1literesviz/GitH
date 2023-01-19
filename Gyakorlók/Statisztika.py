class Nobel:
    def __init__(self,sor:str):
        #Év;Név;SzületésHalálozás;Országkód
        adatok = sor.strip().split(';')
        self.Év = adatok[0]
        self.Név = adatok[1]
        self.SzületésHalálozás = adatok[2]
        self.Országkód = adatok[3]

nobeldijjasok = []
statisztika = dict()

#orszagkodok kigyujtese, mindegyiket csak egyszer

orszagkodok = set()
for nobeldijjas in nobeldijjasok:
    orszagkodok.add(nobeldijjas.OrszágKód)


for orszagkod in orszagkodok:
    statisztika[orszagkod]= 0

print(statisztika)

