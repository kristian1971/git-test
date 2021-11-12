x="U kuhinji je stol. STOL je novi."
x=x.lower()
#print(x)
z=True
while(z):
    prvo=int(x.find("stol"))
    x=x[prvo+1:]
    #y=y+1
    print(prvo)
    if prvo<0:
        z=False
