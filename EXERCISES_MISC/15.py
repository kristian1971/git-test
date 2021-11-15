x=input()
lista=x.split()
listap=[]
listan=[]
for q in range(len(lista)):
    if q==0:
        pass
    elif q%2==0:
        listap.append(str(lista[q]).upper())
    else:
        listan.append(str(lista[q]).lower())

print(listap)
print(listan[:len(listan)-1])
