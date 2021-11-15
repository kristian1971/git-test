dict1={1:1, 2:2}
dict2={3:3, 4:4}
v1=int(input())
v2=int(input())
v3=int(input())
v4=int(input())

dict1.update({1:v1})
dict1.update({2:v2})
dict2.update({3:v3})
dict2.update({4:v4})

dict1.update(dict2)
print(dict1)
