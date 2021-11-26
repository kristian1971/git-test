import re

ulaz=input()

pattern1 = re.compile(r'\d{2,3}')


if pattern1.findall(ulaz)!=[]:
    print("Ima!")


print(pattern1.findall(ulaz))