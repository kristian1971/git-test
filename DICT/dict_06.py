dict1 = {"ime":"pero", "prezime":"perkovic", "godine":42, "spol":"M", "visina":175}
for key in dict1:
    print(f"evo.{key} je {dict1[key]}")

for key, value in dict1.items():
    print(key, value)