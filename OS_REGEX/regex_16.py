import re

ulaz=input()

pattern1 = re.compile(r'fox|dog|horse')

for m in pattern1.finditer(ulaz):
    print(m.start(), m.start()+len(m.group())-1)


#print(pattern1.finditer(ulaz))