"""11. Napišite program koji s tipkovnice učitava cijeli broj n iz intervala [3, 
20]. U slučaju da je unesena vrijednost neispravna, ispisati prikladnu 
poruku na ekran te zatražiti ponovni unos cijelog broja. Nakon 
učitane vrijednosti n, učitajte n parova cijelih brojeva. Nakon što je n
parova brojeva učitano, ispišite parove brojeva koji imaju najveću 
sumu."""

lista1=[]
lista2=[]
indeks=0
suma=0

x=int(input())

while x>20 or x<3:
    print("Nevanja")
    x=int(input())

for broj in range(x):
    prvi=int(input())
    drugi=int(input())
    lista1.append(prvi)
    lista2.append(drugi)
    if prvi+drugi>suma:
        indeks = broj
        suma=prvi+drugi

print(lista1[indeks], lista2[indeks])


