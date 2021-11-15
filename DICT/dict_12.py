dict1={"1":1, "2":2, "3":3, "4":4}

def zbroji(dict1):
    zbroj=0
    for x in dict1:
        zbroj+=dict1[x]
    return zbroj

print(zbroji(dict1))