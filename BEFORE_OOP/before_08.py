"""8. Napišite program koji s tipkovnice učitava proizvoljni cijeli 
troznamenkasti broj. Ako učitani broj nije troznamenkasti, ispišite 
poruku o greški i prekinite daljnje izvođenje programa. U slučaju da 
je učitani broj ispravan, ispišite prvi sljedeći troznamenkasti 
palindrom. Na primjer, ako je učitani broj 120, prvi sljedeći palindrom 
je 121."""
ulaz=input()
if len(ulaz)>3 | len(ulaz)<3:
    print("Greška")
else:
    if ulaz[0]>ulaz[2]:
        ulaz=list(ulaz)
        ulaz[2]=ulaz[0]
    else:
        ulaz=list(ulaz)
        ulaz[1]=str(int(ulaz[1])+1)
        ulaz[2]=ulaz[0]
izlaz=int(ulaz[0])*100+int(ulaz[1])*10+int(ulaz[2])
print(izlaz)
