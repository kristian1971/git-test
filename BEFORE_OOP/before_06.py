"""6. S tipkovnice učitavajte cijele brojeve. Prvi upisani broj može biti bilo 
koji cijeli broj. Učitavanje ponavljati dok god je upisani broj strogo 
veći od prethodno upisanog broja. Ispisati sumu svih učitanih brojeva 
osim broja zbog kojeg je prekinuto učitavanje."""


x = int(input())
zbroj = x
novi = int(input())

while (novi>x):
    zbroj+=novi
    x=novi
    novi=int(input())

print(zbroj)
