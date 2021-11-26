import re

ulaz=input()

pattern1 = re.compile(r'^[0-9a-zA-Z_]*$')


if pattern1.findall(ulaz)!=[]:
    print("Ima!")


print(pattern1.findall(ulaz))