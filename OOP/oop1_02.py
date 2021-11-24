class Stringsve:

    def __init__(self, rijec):
        self.rijec=rijec
        
    def rijec2lista(self):
        return list(self.rijec)

    def kolikoznakova(self):
        return len(self.rijec)-self.rijec.count(" ")

    def int2rim(self):
        pass

    def inverzija(self):
        pass

    def preoblikuj(self):
        pass

    def filtriranje(self):
        pass

rijec1=Stringsve("baka")
rijec2=Stringsve("dida")
print(rijec1.rijec2lista())
print(rijec1.kolikoznakova())