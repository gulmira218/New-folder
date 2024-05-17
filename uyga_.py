

class kitob:
    def __init__(self,muallif,nomi) :
        self.muallif=muallif
        self.nomi=nomi

    def getmuallif(self):
      return self.muallif

    def getnomi(self):
       return self.nomi

    def setmuallif(self,muallif):
        self.muallif = muallif

    def setnomi(self,nomi):
        self.nomi=nomi

    def __str__(self) -> str:
        return f"{self.muallif},{self.nomi}"

    def display(self):
        print("Name:", self.muallif)
        print("Age:", self.nomi)  

    def muallif_ismi(self):
        print(f"muallif_ismi", {self.nomi}) 


class kitob_qushish:
    __kitoblar = {}
    
    def add_kitob(self,muallif,kitob):
        self.__kitoblar[muallif] = kitob 
    def contains(self):
        return len(self.__kitoblar)
    def getInfo(self):
        return self.__kitoblar
    
yangi = kitob_qushish()
yangi.add_kitob("Avloniy","maktab") 


print(yangi.contains())
print(yangi.getInfo())