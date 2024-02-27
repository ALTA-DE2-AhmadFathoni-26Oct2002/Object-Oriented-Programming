# tulis solusi code disini
class ongkos_kirim:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung_ongkos(self):
        if self.panjang*self.lebar*self.tinggi <= 50 and self.berat == 1:
            return "Rp 5000"
    
barang = ongkos_kirim(5,2,4,1)
print(f'Harga : {barang.hitung_ongkos()}')