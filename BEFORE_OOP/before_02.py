"""2. Napravi obrtaljku od unesenog stringa te na svakom drugom mjestu pridruzi nasumičan broj."""
from random import random

unos = input()
obrnuti=unos[::-1]

for x in range(len(unos)):
    if x%2 != 0:
        obrnuti=obrnuti[0:x]+str(int(random()*9))+obrnuti[x+1:]

print(obrnuti)
