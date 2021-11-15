dict1 = {"ime":"pero", "prezime":"perkovic", "godine":42, "spol":"M", "visina":175}

ulaz=input()
izlaz=dict1.get(ulaz)
#print(izlaz)
if(izlaz==None):
    print("Nema tog ključa!")
else:
    print("Ima ključa")
