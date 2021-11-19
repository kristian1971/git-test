"""18. Ispišite sve parne brojeve između 1 i 1000 koju su istovremeno 
djeljivi i s 5 i s 13."""

for x in range(0,1000,5):
    if x%13 == 0:
        print (x)
