# class ichimlik:

#     def __init__(self, nomi ,narxi):
#         self.nomi=nomi
#         self.narxi=narxi


#     def getnomi(self):
#         return self.nomi
    
#     def getnarxi (self):
#         return self.narxi


#     def setnomi(self,nomi):
#         return self.nomi
    
#     def setnarxi (self,narxi):
#         return self.narxi
    

#     def __str__(self) -> str:
#         return f"{self.getnomi()}:{self.getnarxi()}"
    

# class sotuvMashinasi :
#   ichimliklar=[]
#   def addichimlik(self,ichimlik_nomi,ichimlik_narxi):
#       yangi_ichimliklar =ichimlik(ichimlik_nomi,ichimlik_narxi)
#       self.ichimliklar.append(yangi_ichimliklar )
#       for a in self.ichimliklar:
#        print(a)
#   def getPrice(self,nomi):
#       for a in self. ichimliklar:
#         if a.getnomi()== nomi:
#          return(f"{nomi} ning narxi {a.getnarxi()}")  
        
#       return (-1.0)    

# loishsotuvMashinasi=sotuvMashinasi()
# loishsotuvMashinasi.addichimlik("flaves",1000)
# print(loishsotuvMashinasi.getPrice("cola"))      
# print(loishsotuvMashinasi.getPrice("flaves"))



class ichimlik:
    def __init__(self, nomi, narxi,soni):
        self.nomi = nomi
        self.narxi = narxi
        self.soni=soni
    def getNomi(self):
        return self.nomi
    def getNarxi(self):
        return self.narxi
    def setNomi(self, nom):
        self. nomi = nom
    def setNarxi (self, narx):
        self.narxi= narx
    def getSoni(self):
        return self.soni
    def setSoni(self, soni):
        self.son = soni    
    def str (self) ->str :
     return (f"{self.getNomi()}:{self.getNarxi()}:{self.getSoni()}"  )  


class karta:
  def init (self, karta_id, summa):
     self. karta_id = karta_id
     self. summa=summa
  def getId(self):
    return self. karta_id
  def getSumma(self):
    return self. summa
  def setId (self, karta_id) :
    self. karta_id = karta_id
  def setSumma (self, summa):
    self. summa
    self. summa + summa
  def __str__(self)->str:
    return f" {self. getId()}: {self. getSumma()}"  

    # Talab 1 ning 2- va 3- qismlari boshlanayapti
class sotuvMashinasi:
# Talab 1 ning 2 - qismi
  ichimliklar=[] 
  kartalar = [karta("1111", 10000), karta("2222", 20000) ]  
  def addIchimlik(self,ichimlik_nomi,ichimlik_narxi,sonlarichi):
    yangiichimlik=ichimlik(ichimlik_nomi,ichimlik_narxi,sonlarichi)
    self.ichimliklar.append(yangiichimlik)
    for a in self. ichimliklar:
     return(a)
# Talab 1 ning 3gismi
  def getPrice(self, nomi):
   for a in self. ichimliklar:
    if a.getNomi() == nomi:
     return(f" {nomi} ning nari {a. getNarxi()}" )
     return
   return (-1.0)
 

 # Talab 2 ning 2qismi
  def kartaTuldirish(self, card_id, summa):
   for a in self. kartalar:
    if a.getId() ==card_id:
       a. setSumma (summa)
       print((a. getSumma()))
       return "successfully"
   yangi_karta = karta(card_id, summa=summa)
   self. kartalar.append(yangi_karta)
   for i in self. kartalar:
     print (i)
  def getSumma(self, card_id ):
   for a in self. kartalar:
    if a. getId() ==card_id:
        return (f"{card_id} da {a.getSumma()} pul bor")
        return "succsess"
   return (-1.0)
  def sonni(self, sonlari):
   for c in self. ichimliklar:
    if c.getNomi() == sonlari:
     print(f"  {c.getSoni()}" )

  def sotish(self):
   if karta.getId==False  or ichimlik.getNomi==False:
     return  (-1.0)
   if ichimlik.getSoni==False:
     return  (-1.0)
   if ichimlik.getNarxi>karta.getSumma:
     return(-1.0)
   if ichimlik.getNarxi<=karta.getSumma:
     return (karta.getSumma-ichimlik.getNarxi)
     
   
loishsotuvMashinasi=sotuvMashinasi()
loishsotuvMashinasi.addIchimlik("flaves", 1000, 23)
print(loishsotuvMashinasi.sonni("flaves"))



