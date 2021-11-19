"""7. Učitajte s tipkovnice 2 niza znakova, svaki od tih nizova znakova 
spremite u zasebnu varijablu. Ispišite indekse na kojima se pojavljuju 
ista slova neovisno o veličini ('a' i 'A' tretirati jednako)."""

niz1=input().lower()
niz2=input().lower()

if len(niz1)>len(niz2):
    for x in range(len(niz2)):
        if niz1[x]==niz2[x]:
            print(x)
else:
    for x in range(len(niz1)):
        if niz1[x]==niz2[x]:
            print(x)  

