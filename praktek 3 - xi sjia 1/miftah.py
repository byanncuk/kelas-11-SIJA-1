# Praktek 3
# Membuat sebuah sistem sederhana restoran dengan oop
# Interaksi antar objek

class Menuitem:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    def __str__(self):
            return f"{self.nama} - ${self.harga:.2f}"
        
class pelanggan:
    def __init__(self, nama):
         self.nama = nama
         self.pesanan = []
    def pesan(self, menu_item):
        self.pesanan.append(menu_item)
        print(f"{self.nama} memesan {menu_item}")
    def bayar(self):    
        total = sum(item.harga for item in self.pesanan)
        return total
    
class pelayan:
    def __init__(self, nama) :
        self.nama = nama
    def ambil_pesanan(self,pelangan):
        print(f"{self.nama} mengambil pesanan dari {pelanggan.nama}")
    def antar_pesanan(self, pelanggan):
        total = pelanggan.bayar()
        print(f"{self.nama} menghantarkan pesanan kepada {pelanggan.nama}") 
        print(f"total tagihan : ${total:.2f}")
        
class dapur:
    def __init__(self):
        self.menu = {
            "Burger" : Menuitem("burger", 5.99),
            "Pasta" : Menuitem("Pasta", 7.99),
            "Pizza" : Menuitem("Pizza", 8.99)
        }
    def Siapkan_pesanan(self, pesanan):
        for item in pesanan:
            if item.nama in self.menu:
                print(f"menyediakan {item} dengan harga ${item.harga:.2f}")
            else:
                print(f"{item.nama} tidak ada dalam menu")
                
pelanggan = pelanggan("alice")
pelayan = pelayan("bob")
dapur = dapur()

burger = Menuitem("Burger",5,99)
pizza =Menuitem("pizza", 8,99)

pelanggan.pesan(burger)
pelanggan.pesan(pizza)

pelayan.ambil_pesanan(pelanggan)
dapur.Siapkan_pesanan(pelanggan.pesanan)

pelayan.antar_pesanan(pelanggan)                                        