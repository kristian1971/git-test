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