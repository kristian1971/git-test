"""3.  Napiši program koji upisuje bodove n plesnih natjecanja. Ispiši zbroj svih bodova tako da odbaciš 
najbolji i najlošiji rezultat."""

n=int(input("Koliko je bilo natjecanja?"))
lista=[]
zbroj = 0

for x in range(n):
    lista.append(input())

lista.remove(min(lista))
lista.remove(max(lista))

for x in range(len(lista)):
    zbroj+=int(lista[x])

print(zbroj)

