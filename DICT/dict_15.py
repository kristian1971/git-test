dict1 = {"ime":"pero", "nadimak1":"pero1", "prezime":42, "godine":42, "spol":"M", "visina":175, "nadimak":"pero", "nadimak2":"pero1"}
#lista1=list(dict.from)
n=len(dict1)
brojac=len(dict1)
list1=list(dict1)
list2=list(dict1.values())
start=0
while(brojac>0):
    for x in range(start+1,n):
        if list2[start]==list2[x]:
            list1.pop(x)
            list2.pop(x)
            list1.pop(start)
            list2.pop(start)
            n=len(list1)
            start=0
            break
    brojac=brojac-1

# print(dict1)
print(list1)
print(list2)
nova=dict(zip(list1, list2))
print(nova)