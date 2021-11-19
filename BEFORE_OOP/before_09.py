"""9. Napišite program koji učitava cijele brojeve sve dok je unesena 
vrijednost veća od 0. Pronađite koji od učitanih brojeva ima najmanju 
sumu znamenki te ispišite taj broj i sumu."""

lista = []

x = input()
final_najmanji_broj = x

zbrojod_najmanjeg=0
for mali in range(len(x)):
    zbrojod_najmanjeg = zbrojod_najmanjeg + int(x[mali])
final_zbrojod_najmanjeg = zbrojod_najmanjeg
zbrojod_najmanjeg=0

while(int(x)>0):
    lista.append(x)
    x = input()

for brojac in range(1,len(lista)):
    for mali in range(len(lista[brojac])):
        zbrojod_najmanjeg = zbrojod_najmanjeg + int(lista[brojac][mali])
    if zbrojod_najmanjeg < final_zbrojod_najmanjeg:
        final_zbrojod_najmanjeg = zbrojod_najmanjeg
        final_najmanji_broj=lista[brojac]
    zbrojod_najmanjeg=0

print (final_najmanji_broj, final_zbrojod_najmanjeg)