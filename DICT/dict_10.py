dict1={}

def generiraj(n):
    for x in range(1,n+1):
        #dict1.setdefault(x,x*x)
        dict1[x]=x*x
n=int(input())
generiraj(n)
print(dict1)