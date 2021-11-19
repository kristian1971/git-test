"""17. Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni niz 
znakova. Ispišite koliko velikih slova se nalazi u nizu. Ako je neko od 
unesenih slova u nizu "A", brojanje velikih slova je potrebno prekinuti 
i ispisati informaciju da je veliko slovo "A" pronađeno."""

niz="gdfhfBGDjdksgHFDkdhsAdhkshdskhADGGK"
brojac = 0

for x in range(len(niz)):
    if niz[x].isupper() and niz[x] != "A":
        brojac+=1
    elif niz[x].isupper() and niz[x] == "A":
        print("Nasao A")
        break
    else:
        pass

print(brojac)
