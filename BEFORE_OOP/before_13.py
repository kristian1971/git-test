"""13. Napišite program koji će inicijalizirati varijablu n na proizvoljnu 
cjelobrojnu vrijednost. Vrijednost varijable n neka predstavlja red 
tablice. Ispisati tablicu veličine n redaka i n stupaca. Vrijednost 1 
neka se nalazi na glavnoj dijagonali, a vrijednost 0 na svim ostalim 
mjestima. U nastavku slijedi primjer za n=5:
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1

Napomena: za ispis vrijednost, tako da se nakon ispisa vrijednosti 
dane print() funkciji ne ispiše novi redak koristiti sljedeću 
sintaksu: print(vrijednost, end='')"""
from random import random

n = int(random()*10+2)
brojac = 0

for x in range (0,n):
    for y in range (0,n):
        if y == brojac:
            print("1", end='')
        else:
            print("0", end = '')
    brojac+=1
    print("")

    
