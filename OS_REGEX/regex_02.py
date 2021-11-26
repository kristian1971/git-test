import re

ulaz=input()

pattern1 = re.compile(r'a0')
pattern2 = re.compile(r'b{2,}')

if pattern1.findall(ulaz)!=[] or pattern2.findall(ulaz)!=[]:
    print("Ima!")

