class Zivotinja:

    def __init__(self, vrsta_ishrane, naziv, vrsta, broj_nogu):
        self.vrsta_ishrane=vrsta_ishrane
        self.naziv=naziv
        self.vrsta=vrsta
        self.broj_nogu=broj_nogu

    def test(self):
        print(self.naziv, self.broj_nogu)

    def ispisi_sve(self):
        print(self.naziv, self.vrsta_ishrane, self.vrsta, self.broj_nogu)

class LetecaZivotinja(Zivotinja):

    def __init__(self, vrsta_ishrane, naziv, vrsta, broj_nogu, raspon_krila, broj_jaja):
        super().__init__(vrsta_ishrane, naziv, vrsta, broj_nogu)
        self.raspon_krila = raspon_krila
        self.broj_jaja=broj_jaja

    def ispisi_sve(self):
        print(self.naziv, self.vrsta_ishrane, self.vrsta, self.broj_nogu, self.raspon_krila, self.broj_jaja)

class MorskaZivotinja(Zivotinja):

    Zivotinja

kit=Zivotinja("mesojed", "kit", "ribe", 0)
kokos=Zivotinja("biljojed", "kokos", "ptica", 2)

kit.ispisi_sve()

z_vrsta=LetecaZivotinja("biljojed", "kokos", "ptica", 2, 42, 45)
z_vrsta.ispisi_sve()