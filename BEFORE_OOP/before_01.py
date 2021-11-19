"""1. Napiši program koji učitava listu i briše sve duplikate iz te liste te ispisuje novu listu s 
obrisanim duplikatima."""

lista1 = [1,2,3,2,1,2,3,2,1]
set_convert = set(lista1)
lista2 = list(set_convert)
print(lista2)