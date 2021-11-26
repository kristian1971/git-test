import re

ulaz=input()

pattern1 = re.compile(r'\b\w*$')


if pattern1.findall(ulaz)!=[]:
    print("Ima!")


print(pattern1.findall(ulaz))