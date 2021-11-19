"""20. Napisi program koji unosi n brojeva i sastavlja novi broj od najvece znamenke u svakom od
brojevaS"""

n = int(input())
novi=str('')

for x in range(n):
    broj=input()
    desetica=max(broj)
    novi+=desetica

print(novi)