"""12. Napišite program koji s tipkovnice učitava proizvoljni niz znakova. 
Nad učitanim nizom znakova napravite analizu je li taj niz palindrom 
ili nije. Niz je palindrom ako se isto čita slijeva nadesno ili pak 
zdesna nalijevo."""

ulaz = input()
izlaz = ulaz[::-1]
if ulaz==izlaz:
    print("Palindrom")

