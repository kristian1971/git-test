"""19. Napisi program koji unosi n brojeva i od znamenke desetice svakog broja stvara novi broj."""

n = int(input())
novi=str('')

for x in range(n):
    broj=input()
    desetica=broj[-2]
    novi+=desetica

print(novi)
