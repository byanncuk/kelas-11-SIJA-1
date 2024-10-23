class Mobil:
    def __init__(self, merk, model, tahun):
        self.__merk = merk 
        self.__model = model
        self.__tahun = tahun
        
    def get_merk(self):
        return self.__merk
    
    def set_merk(self ,merk):
        self.__merk = merk
        
    def get_model(self):
        return self.__model
    
    def set_model(self ,model):
        self.__model = model
        
    def get_tahun(self):
        return self.__tahun
    
    def set_tahun(self ,tahun):
        if tahun > 1885:
            self.__tahun = tahun
        else:
            print("Tahun tidak valid untuk mobil") 
            
mobil1 = Mobil("toyota","corlla",2020)

print(mobil1.get_merk())
mobil1.set_tahun(2020)
print(mobil1.get_tahun())                       