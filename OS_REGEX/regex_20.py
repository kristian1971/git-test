import re

eu_datum=input()

pattern1 = re.compile(r'^\d{1,2}')
dan=re.findall(pattern1, eu_datum)
print(dan)

pattern2 = re.compile(r'\.\d{1,2}\.')
mjesec = re.findall(pattern2, eu_datum)
mjesec[0]=mjesec[0][1:3]
print(mjesec)

pattern3 = re.compile(r'\d{4}$')
godina = re.findall(pattern3, eu_datum)
print(godina)

izlaz=[]
izlaz.append(mjesec)
izlaz.append(dan)
izlaz.append(godina)

izlaz2=str(mjesec[0])+"."+str(dan[0])+"."+str(godina[0])

print(izlaz2)