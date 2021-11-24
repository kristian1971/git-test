f=open("file02.txt", "w")
unos = input()
while unos != "!#quit$":
    f.write(unos)
    f.write("\n")
    unos = input()
#f.write("Dobro\n")
f.close()