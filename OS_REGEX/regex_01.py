text = '''
    asdfhjlkjhkjhkjhkjhfasdfa
    ASDFKJSLAKDFJALSKDFJALSKDFJ
    1435468545

    JKhkjKJHKJhjk
    lkj LKFSDJALKlkj KJLKJsaf sadf 6544


    Meta characteri: . ^ $ * + ? { } [ ] \ | ( )


    dariokarl.sl@gmail.com

    034-561-0564
    034/556 1231
    +385911234567

    www.aicentarlipik.com

    Pero Perić

    gđa. Ruslan

    Kljukica Kvakić kvakvakva

    g. Hrvoje Hrvač

'''
import re

pattern = re.compile(r'[A-Z]')
matches1 = pattern.findall(text)
velika=len(matches1)

pattern = re.compile(r'[a-z]')
matches2 = pattern.findall(text)
mala=len(matches2)

pattern = re.compile(r'[0-9]')
matches3 = pattern.findall(text)
brojevi=len(matches3)

print(f"velika {velika}, mala {mala}, brojevi {brojevi}")