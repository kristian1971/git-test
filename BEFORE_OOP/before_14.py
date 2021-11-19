"""14. Odaberite proizvoljno koordinatu T=(x,y), vrijednosti varijabli x
(stupac) i y (redak) neka budu manje od 10. Program neka ispiše 
polje 10x10 čiji su svi elementi vrijednosti "-" osim koordinate T čija 
je vrijednost "X". 

Primjer: T=(1,1)
- - - - - - - - - -
- X - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -S"""

stupac = 5
redak = 3

for x in range (0,10):
    for y in range (0,10):
        if y == stupac and x==redak:
            print("X", end='')
        else:
            print("-", end = '')
    print("")

    