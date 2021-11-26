import re

ulaz=input()

pattern1 = re.compile(r'[a-z]+_.[a-z]+')


if pattern1.findall(ulaz)!=[]:
    print("Ima!")


print(pattern1.findall(ulaz))