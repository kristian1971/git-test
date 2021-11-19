"""5. Kreiraj listu koja se sastoji od stringova i brojeva, te odvoji brojeve i stringove u zasebne liste"""

lista = [1, "a", 2, "b", 3, "c"]

lista_b=[]
lista_s=[]

for x in range(len(lista)):
    if type(lista[x])==int:
        lista_b.append(lista[x])
    else:
        lista_s.append(lista[x])

print(lista_b, lista_s)