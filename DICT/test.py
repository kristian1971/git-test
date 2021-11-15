d={"ime":"Daniel", "prezime":"Ivic", "godine":50, "ima_potvrdu":False}
e={"broj":42}
d.update(e)
print(d.keys())
print(d.values())
print(d.items())

print(d["ime"])
print(d.get("ime"))
#d=d+e