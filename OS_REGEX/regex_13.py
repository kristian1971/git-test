#Tu se valjda misli sa početka svakog od 4 dijela IP adrese

import re

ulaz=input()

pattern1 = '\.[0]*'

ip=re.sub(pattern1,".",ulaz)


print(ip)