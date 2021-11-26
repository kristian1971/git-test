import re

ulaz=input()

pattern1 = re.compile(r'a[b{1,2}]')


if pattern1.findall(ulaz)!=[]:
    print("Ima!")


print(pattern1.findall(ulaz))