dict1={"1":1, "2":2, "3":3, "4":4}


def trazi(dict1):
    min=int(list(dict1.values())[0])
    max=int(list(dict1.values())[0])
    for x in dict1:
        if dict1[x]>max:
            max=dict1[x]
        if dict1[x]<min:
            min=dict1[x]
    return min, max

povrat=trazi(dict1)
prvi=povrat[0]
drugi=povrat[1]
print(f"Namjanji je {prvi}, a najveći {drugi}")