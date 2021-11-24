class Zivotinja:

    def __init__(self, naziv, tip, masa, ishrana):
        self.naziv = naziv
        self.tip=tip
        self.masa = masa
        self.ishrana=ishrana

    def ispisi(self):
        print(self.naziv)
        print(self.tip)
        print(self.masa)
        print(self.ishrana)
    
ziv1=Zivotinja("zec","brzi","laka","mrkva")
ziv2=Zivotinja("lav", "brza", "težak", "zec")

ziv1.ispisi()
ziv2.ispisi()