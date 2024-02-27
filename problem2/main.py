# tulis solusi code disini
class bangundatar:
    def __init__(self, panjang):
        self.panjang = panjang

class kubus(bangundatar):
    def __init__(self, panjang):
        super().__init__(panjang)
    
    def volumekubus(self):
        return self.panjang*self.panjang*self.panjang
    
class balok(bangundatar):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__(panjang)
        self.lebar = lebar
        self.tinggi = tinggi
    
    def volumebalok(self):
        return self.panjang*self.lebar*self.tinggi
    
class tabung(bangundatar):
    def __init__(self, panjang, tinggi):
        super().__init__(panjang)
        self.tinggi = tinggi
    
    def volumetabung(self):
        return int(22/7*(self.panjang**2)*self.tinggi)
    

volume_kubus = kubus(10)
volume_balok = balok(3,6,10)
volume_tabung = tabung(7,10)

print(f'Kubus : {volume_kubus.volumekubus()}')
print(f'Balok : {volume_balok.volumebalok()}')
print(f'Tabung : {volume_tabung.volumetabung()}')  
        