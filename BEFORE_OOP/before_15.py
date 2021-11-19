"""15. Napišite program koji ispisuje koliko ima prostih brojeva između 
dva proizvoljna broja (prost broj je broj koji je djeljiv samo sa 1 i sa samim sobom).S"""

x= 3
y=33
prim=0

for q in range(x,y+1):
    for z in range(1,q+1):
        if q%z==0:
            prim+=1
    if prim==2:
        print(q)
    prim=0

