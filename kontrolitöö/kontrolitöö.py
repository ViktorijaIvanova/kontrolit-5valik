print("5 valik")


#harjutus 1
maja=[  "  ~~~~~",
      " /_____\ ",
      " | []  |",
       "  -----"]
n = 9
for i in maja:
    print(i*n)

#harjutus 2
import math
Aklass=int(input("Sisestage õpilaste arv:" ))
p = 0
for i in range(Aklass):
 a = int(input("Sisetage hinne:" ))
p=p/20.0
p=p+a
print(a)
print("Õpilaste keskmine hinne={0:2f}".format(p))  
 

#harjutus 5
x_max,x_min, step = 3, 1, 0.5
x_values = [x_min + step*i for i in range(int((x_max - x_min)/step) + 1)]
y_values = [-0.5 * x + x for x in x_values]
print("x\t\t\ty")
for  y in zip(y_values):
    print(f"{y}\t")
    for  x in zip(x_values):
      print(f"{x}\t")
print()
print("See on lõpp")



 #harjutus 3
import random
õpilased= random.randint(5, 15)
print("õpilased:" )
hinne = ()
for i in range(õpilased):
    a = random.randint(1, 5) #see on hind
    a = int(input("hind:"))
maksimalset = hinne(0)
minimalset = hinne(0)
for hinne in hinne:
    if hinne > maksimalselt:
        maksimalselt= hinne
    elif hinne < minimalselt:
        minimalselt = hinne
print(f"minimalselt hinne:",minimalselt  )
print(f"maksimalselt hinne:",maksimalselt )
print()
print()



