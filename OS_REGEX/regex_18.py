ulaz ="Python exercises, PHP exercises, C# exercises"

import re


pattern1 = re.compile(r'exercises')

for m in pattern1.finditer(ulaz):
    print(m.start(), m.start()+len(m.group())-1)