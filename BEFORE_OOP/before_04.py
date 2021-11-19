"""4. Kreiraj listu brojeva i pretvori svaki element u listi u njegov kvadrat"""

lista = [1,2,3,4]

for x in range(len(lista)):
    lista[x]=lista[x]*lista[x]

print(lista)