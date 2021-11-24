izbor = input("Unesite žanr knjige")
izbor+=".txt"
f=open(izbor,"r+")
josjedna="d"

izbor2=input("Unesite 1 za dodavanje, 2 za ispis i 3 za izlaz")
while izbor2=="1" or izbor2=="2":
    if izbor2=="1": 
        while josjedna=="d":
            naslov=input("Naslov")
            autor=input("Autor")
            godina=input("Godina")
            cijena=input("Cijena")
            sve=naslov+","+autor+","+godina+","+cijena+"\n"
            f.write(sve)
            josjedna=input("Još jednu? d/n")
    if izbor2=="2":
        for l in f:
            print(l)
    izbor2=input("Unesite 1 za dodavanje, 2 za ispis i 3 za izlaz")

f.close()