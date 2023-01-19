# a<=b<=c
# a2 + b2 = c2 derekszog
# a2 + b2  > c2 hegyesszog
# a2 + b2 < c3 tompaszogu
a= float(input("Add meg az oldal méretét: "))
b= float(input("Add meg a második oldal méretét: "))
c= float(input("Add meg a harmadik oldal méretét"))
if a**2 + b**2 > c**2:
    print("Hegyesszögű")
elif  a**2 + b**2 == c**2:
    print("derekszog")
else:
    print("Tompaszogu")


