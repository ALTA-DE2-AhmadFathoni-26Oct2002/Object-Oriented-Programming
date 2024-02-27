# tulis solusi code disini
class bangundatar:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

class luas(bangundatar):
    def __init__(self, panjang, lebar):
        super().__init__(panjang, lebar)

    def luaspersegi(self):
        return self.panjang * self.panjang

    def luassegitiga(self):
        return (self.panjang * self.lebar)//2
    
    def luaspersegipanjang(self):
        return self.panjang * self.lebar
    
persegi = luas(4, 0)
segitiga = luas(3, 4)
persegipanjang = luas(7, 8)
    
print ("Luas")
print('Persegi : ', persegi.luaspersegi())
print('Segitiga : ', segitiga.luassegitiga())
print('Persegi Panjang : ', persegipanjang.luaspersegipanjang())
    
class keliling(bangundatar):
    def __init__(self, panjang, lebar):
        super().__init__(panjang, lebar)


    def kelilingpersegi(self):
        return self.panjang * 4

    def kelilingsegitiga(self):
        return self.panjang * self.lebar
    
    def kelilingpersegipanjang(self):
        return (self.panjang + self.lebar) * 2
    

persegi = keliling(4, 0)
segitiga = keliling(3, 4)
persegipanjang = keliling(7, 8)

print ("keliling")
print('Persegi : ', persegi.kelilingpersegi())
print('Segitiga : ', segitiga.kelilingsegitiga())
print('Persegi Panjang : ', persegipanjang.kelilingpersegipanjang())