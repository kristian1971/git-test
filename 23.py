
def pira(x):
    lista=[]
    for brojac in range(0,x):
        lista.append([])
        for malibrojac in range(0,brojac):
            lista[brojac].append(1)
    return lista

izlaz=pira(int(input())) 
print(izlaz)