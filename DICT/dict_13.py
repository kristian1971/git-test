dict1={"data1":100, "data2":-54, "data3":247}

def mnozi(dict1):
    umn=1
    for x in dict1:
        umn*=dict1[x]
    return umn

print(mnozi(dict1))