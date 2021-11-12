def funkcija(lista):
    #definicije varijabli
    umn=int(1)
    zbr=int(0)
    listaprim=[]
    listapar=[]
    nprim=False

    #umnozak
    for q in range(len(lista)):
        umn*=int(lista[q])
    #print(umn)

    #zbroj
    for q in range(len(lista)):
        zbr+=int(lista[q])
    #print(zbr)

    #sortiranje
    listasort=lista
    listasort.sort(reverse=True)
    #print(listasort)

    #prim brojevi
    for q in range(0, len(lista)):
        for i in range(2, int(lista[q])):
            if(int(lista[q])%i)==0:
                nprim=True
                break
        if(nprim):
            nprim=False
            pass
        else:
            listaprim.append(lista[q])
            nprim=False
    #print(listaprim)

    #parni brojevi
    for q in range (0, len(lista)):
        if(int(lista[q])%2==0):
            listapar.append(lista[q])

    #print(listapar)
    return umn, zbr, listasort, tuple(listaprim), tuple(listapar)

lista=[]
x=input()

while(x.isnumeric()):
    lista.append(x)
    x=input()

i,j,k,l,m=funkcija(lista)
print(i,j,k,l,m)

f=open("test.txt","a")
f.write(str(i))
f.write(str(j))
f.write(str(k))
f.write(str(l))
f.write(str(m))
f.close()






