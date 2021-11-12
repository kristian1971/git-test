
def pira(x):
    lista=[]
    malalista=[]
    for brojac in range(0,x):
        for malibrojac in range(0,brojac):
            malalista.append(1)
        lista.append(malalista)
        malalista.clear()
    return lista

izlaz=pira(int(input())) 
print(izlaz)