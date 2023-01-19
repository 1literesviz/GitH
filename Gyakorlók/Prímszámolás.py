#
# def isprim():
#     szám= int(input("Kérek egy számot"))
#     vanoszto = False
#     oszto = 2
#     while oszto < szám and not vanoszto:
#         if szám % oszto == 0:
#             vanoszto = True
#         oszto += 1
    
#     if vanoszto:            
#         print("Nem prím.")
#     elif vanoszto == 2:
#         print("Nem prím")
#     else:
#         print("Prím.")
# print(isprim())


def prim(szam):
    osztodb = 0
    for i in range (1,szam+1):
        if szam%i ==0:
            osztodb+=1
    if osztodb==2:
        return True
    else:
        return False
    
lista = [4,3,5,6,2,8,1]
for i in range(len(lista)):
    if prim(i):
        print(lista[i], end=',')
