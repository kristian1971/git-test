class Kalkulator:

    def __init__(self, a, b):
        self.a=a
        self.b=b
    
    def zbroji(self, ime):
        print(ime)
        return self.a+self.b

    @staticmethod
    def mnozi(x, y):
        print(x*y)


k1=Kalkulator(22,33)
#print(k1.zbroji("ggdd"))
#print(k1.a, k1.b)

def primjer(a, *args):
    print(a)
    print(args)

primjer(2,3,4,5)

def primjer2(a, **kwargs):
    print(a)
    print(kwargs)

primjer2(2, ime="dani")

