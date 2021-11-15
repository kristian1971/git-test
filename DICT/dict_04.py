dict1 = {"ime":"pero", "prezime":"perkovic", "godine":42}
print(dict1.setdefault("ime"), dict1.setdefault("prezime"))
dict1.setdefault("visina",175)
print(dict1)