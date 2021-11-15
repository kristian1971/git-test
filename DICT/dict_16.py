dict1 = {"zec":"rabbit", "pas":"dog", "auto":"car", "lice":"face", "lav":"lion"}

ulaz=input().lower()
while(ulaz!="x"):
    if(dict1.get(ulaz)!=None):
        print(dict1.get(ulaz))
    else:
        print("No word")
    ulaz=input().lower()

