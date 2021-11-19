"""10. S tipkovnice učitajte proizvoljni niz znakova. Kreirajte novi niz 
znakova koji će sadržavati naizmjence velika i mala slova iz ulaznog 
niza, redom kako se pojavljuju u ulaznom nizu: prvo veliko slovo u 
ulaznom nizu, prvo sljedeće malo slovo u nastavku ulaznog niza, 
prvo sljedeće veliko slovo u nastavku ulaznog niza itd. Novokreirani 
niz ispišite na zaslon. U nastavku se nalazi primjer:

Ulazni niz: ifeFemFEkej83FkW
Izlazni niz: FeFkFkW"""

ulaz = list(input())
novi = []
veliko=False
test = True
print(ulaz)

for x in range(len(ulaz)):
    if ( ulaz[x].isupper() and veliko==False):
        novi.append(ulaz[x])
        veliko=True
    elif (ulaz[x].islower() and veliko==True):
        novi.append(ulaz[x])
        veliko=False
    else:
        pass

print(novi)

    