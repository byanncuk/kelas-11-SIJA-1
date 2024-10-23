class Hewan:
    def suara(self):
        raise NotImplementedError("Subclass harus mengimplemetasikan metode ini")
    
class kucing(Hewan):
    def suara(self):
        return "MIAUUUUUUU"
    
class sapi(Hewan):
    def suara(self):
        return "moo"      
    
def cetak_suara(hewan):  
    print(hewan.suara())
    