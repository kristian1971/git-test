f=open("file.txt", "r")
"""d=f.readline()
print(d)
d=f.readline()
print(d)"""
for l in f:
    print(l)
f.close()