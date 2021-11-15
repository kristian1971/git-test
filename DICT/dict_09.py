dict1 = {"ime":"pero", "prezime":"perkovic", "godine":42, "spol":"M", "visina":175}

def provjera(rije):
    for key, value in rije.items():
        print(key, value)


provjera(dict1)