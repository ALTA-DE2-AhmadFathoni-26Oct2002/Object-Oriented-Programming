# tulis solusi code disini
class kalkulator:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

class penjumlahan(kalkulator):
    def __init__(self, angka1, angka2):
        super().__init__(angka1, angka2)
    
    def jumlah(self):
        return self.angka1 + self.angka2
    
class pengurangan(kalkulator):
    def __init__(self, angka1, angka2):
        super().__init__(angka1, angka2)
    
    def kurang(self):
        return self.angka1 - self.angka2
    
class perkalian(kalkulator):
    def __init__(self, angka1, angka2):
        super().__init__(angka1, angka2)
    
    def kali(self):
        return self.angka1 * self.angka2
    
class pembagian(kalkulator):
    def __init__(self, angka1, angka2):
        super().__init__(angka1, angka2)
    
    def bagi(self):
        return self.angka1 // self.angka2
    

angka_jumlah = penjumlahan(3,4)
angka_kurang = pengurangan(15,4)
angka_kali = perkalian(10,10)
angka_bagi = pembagian(12,3)

print(f'Penjumlahan : {angka_jumlah.jumlah()}')
print(f'Pengurangan : {angka_kurang.kurang()}')
print(f'Perkalian : {angka_kali.kali()}')
print(f'Pembagian : {angka_bagi.bagi()}')