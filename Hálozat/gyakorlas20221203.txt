from functions import *

fajlbeolvasas()
print(f"3.feladat : {len(nobeldijjasok)}")


statisztika = dict()

#orszagkodok kigyujtese, mindegyiket csak egyszer

orszagkodok = set()
for nobeldijjas in nobeldijjasok:
    orszagkodok.add(nobeldijjas.Országkód)


for orszagkod in orszagkodok:
    statisztika[orszagkod]= 0

for nobeldijjas in nobeldijjasok:
    statisztika[nobeldijjas.Országkód]+=1



for nobeldijjas in nobeldijjasok:
    if nobeldijjas.Országkód in statisztika:
        statisztika[nobeldijjas.Országkód]+=1
    else:
        statisztika[nobeldijjas.Országkód] = 1
for key, value in statisztika.items():
    if value >5:
        print(f"{key} - {value}")


print(statisztika)


print(f"4.Feladat : Utolsó év : {utolsóév()}")

print(f"5.Feladat:Kérem adja meg egy ország kódját: {orszagKod}")
