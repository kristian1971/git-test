str="Testiramo što sve možemo napraviti sa stringovima"
rijec="string"
gdje_je=str.find(rijec)

print(gdje_je)

matrix =[]
"""
for i in range(5):
    l=[]
    for j in range(5):
        l.append(j)
    matrix.append(l)
print(matrix)
"""

matrix=[[j for j in range(5)]for i in range(5)]
print(matrix)

matrix2=[[1,2,3], [4,5],[6,7,8,9]]

flat_list=[]
for sublist in matrix2:
    for item in sublist:
        flat_list.append(item)
#flat_list1=[]
flat_list1=[item for sublist in matrix2 for item in sublist ]
print(flat_list1)

flat_list2=[item  for item in sublist for sublist in matrix2]
print(flat_list2)

def pyramid(x):
    l=[]
    for i in range(1,x+1):
        l.append([1]*i)
    print(l)

#%%
print("ts")



# %%

x=isinstance(5, int)
print(x)
y=isinstance(5, str)
print(y)


# %%
import os
#print(dir(os))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())
# %%
