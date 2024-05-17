# a=10
# son=0
# for z in range(a+1):
#     if z %3 ==0:
#       son =son+1
      
#       print(son) 

# class VendingMachine:
#     def __init__(self, num_columns):
#         self.columns = [{} for _ in range(num_columns)]  # Har bir ustunni ichimliklar bilan boshlang
#         self.prices = {}  # Ichimlik narxlari

#     def addBeverage(self, column, name, price):
#         """Yangi ichimlik qo'shish"""
#         if column < 0 or column >= len(self.columns):
#             return "Noto'g'ri ustun raqami"
#         self.columns[column][name] = 0  # Yangi ichimlikni qo'shamiz
#         self.prices[name] = price  # Ichimlik narxini saqlash

#     def getPrice(self, name):
#         """Ichimlik narxini olish"""
#         return self.prices.get(name, -1.0)  # Agar ichimlik mavjud bo'lmasa -1.0 qaytariladi

#     def rechargeCard(self, card_id, amount):
#         """Kartani to'ldirish"""
#         # Kartaning kreditini olish (mavjud bo'lmasa -1.0)
#         current_credit = self.getCredit(card_id)
#         if current_credit == -1.0:
#             self.cards[card_id] = amount
#         else:
#             self.cards[card_id] += amount

#     def getCredit(self, card_id):
#         """Kartaning kreditini olish"""
#         return self.cards.get(card_id, -1.0)  # Agar karta mavjud bo'lmasa -1.0 qaytariladi

#     def refillColumn(self, column, name, quantity):
#         """Ustunni ichimliklar bilan to'ldirish"""
#         if column < 0 or column >= len(self.columns):
#             return "Noto'g'ri ustun raqami"
#         if name not in self.prices:
#             return "Ichimlik mavjud emas"
#         self.columns[column][name] += quantity

# # Mashinani 4 ta ustundan tuzamiz
# mashina = VendingMachine(num_columns=4)

# # Ichimliklarni qo'shamiz
# mashina.addBeverage(column=0, name="Coca Cola", price=3200)
# mashina.addBeverage(column=1, name="Suv", price=1000)
# mashina.addBeverage(column=2, name="Pepsi", price=2500)

# # Kartalarni to'ldiramiz
# mashina.rechargeCard(card_id=12, amount=12000)
# mashina.rechargeCard(card_id=21, amount=5600)
# mashina.rechargeCard(card_id=99, amount=15800)

# # Ichimliklar bilan ustunlarni to'ldiramiz
# mashina.refillColumn(column=0, name="Coca Cola", quantity=10)
# mashina.refillColumn(column=1, name="Suv", quantity=20)
# mashina.refillColumn(column=2, name="Pepsi", quantity=15)




"""class Ichimlik:
    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.narxi = narxi

    def narxniOlish(self):
        return self.narxi

class Karta:
    def __init__(self, karta_id, hisob):
        self.karta_id = karta_id
        self.hisob = hisob

    def summaniOlish(self):
        return self.hisob

class ichimlikSotibOlishMashinasi:
    def __init__(self):
        self.ichimliklar = []
        self.kartalar = []
        self.ustunlar = []

    def ichimlikQoshish(self, ichimlik):
        self.ichimliklar.append(ichimlik)

    def kartaQoshish(self, karta):
        mavjud_karta = next((k for k in self.kartalar if k.karta_id == karta.karta_id), None)
        if mavjud_karta:
            mavjud_karta.hisob += karta.hisob
        else:
            self.kartalar.append(karta)

    def ustunniToldirish(self, ustun, ichimlik, miqdori):
        self.ustunlar.append({'nomi': ichimlik.nomi, 'miqdori': miqdori})

    def borIchimliklar(self, ichimlik_nomi):
        miqdor = sum(ustun['miqdori'] for ustun in self.ustunlar if ustun['nomi'] == ichimlik_nomi)
        return miqdor
    

    def sotish(self, ichimlik_nomi, karta_id):
        for ustun_raqami, ustun in enumerate(self.ustunlar):
            if ustun['nomi'] == ichimlik_nomi and ustun['miqdori'] > 0:
                tanlangan_ichimlik = next((i for i in self.ichimliklar if i.nomi == ichimlik_nomi), None)

                tanlangan_karta = next((k for k in self.kartalar if k.karta_id == karta_id), None)
                if tanlangan_karta and tanlangan_karta.hisob >= tanlangan_ichimlik.narxi:
                    tanlangan_karta.hisob -= tanlangan_ichimlik.narxi
                    self.ustunlar[ustun_raqami]['miqdori'] -= 1
                    return ustun_raqami + 1  
                else:
                    return -1.0  
        return -1.0  

if __name__ == "__main__":
   
    cola = Ichimlik("Coca Cola", 3200)
    suv = Ichimlik("Suv", 1000)
    pepsi = Ichimlik("Pepsi", 2500)

    
    karta1 = Karta(12, 12000)
    karta2 = Karta(21, 5600)
    karta3 = Karta(99, 15800)
    


    a = ichimlikSotibOlishMashinasi()



    a.ichimlikQoshish(cola)
    a.ichimlikQoshish(suv)
    a.ichimlikQoshish(pepsi)


    a.kartaQoshish(karta1)
    a.kartaQoshish(karta2)
    a.kartaQoshish(karta3)
    
    a.ustunniToldirish(1, cola, 1)
    a.ustunniToldirish(2, suv, 10)
    a.ustunniToldirish(3, pepsi, 15)
    a.ustunniToldirish(4, suv, 20)


 
    print(a.sotish("Coca Cola", 12)) 
    print(a.sotish("Coca Cola", 4)) 
    print(a.sotish("Pepsi", 99))"""



class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __str__(self):
        return f"{self.author}, {self.title}"

class Shelf:
    def __init__(self, code):
        self.code = code
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def contains(self, book):
        return book in self.books

    def get_books(self):
        shelf_info = f"Shelf {self.code}\n"
        for book in self.books:
            shelf_info += str(book) + "\n"
        return shelf_info

class Library:
    def __init__(self):
        self.shelves = {}

    def add_shelf(self, code):
        if code not in self.shelves:
            self.shelves[code] = Shelf(code)

    def add_book(self, book, shelf_code):
        if shelf_code in self.shelves:
            self.shelves[shelf_code].add_book(book)

    def find_book(self, author, title):
        for shelf in self.shelves.values():
            for book in shelf.books:
                if book.author == author and book.title == title:
                    return shelf.code
        return None

    def get_books_from_shelf(self, shelf_code):
        if shelf_code in self.shelves:
            return self.shelves[shelf_code].get_books()
        else:
            return "Shelf not found"

# Example usage:
library = Library()
library.add_shelf("C1")
library.add_book(Book("John Doe", "Python Basics"), "C1")
library.add_book(Book("Jane Smith", "Java for Beginners"), "C1")
print(library.get_books_from_shelf("C1"))
print(library.find_book("John Doe", "Python Basics"))

class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __str__(self):
        return f"{self.author}, {self.title}"

    def get_author(self):
        return self.author

    def get_title(self):
        return self.title


class Shelf:
    def __init__(self, code):
        self.code = code
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def contains(self, book):
        return book in self.books

    def get_books(self):
        shelf_info = f"Shelf {self.code}\n"
        for book in self.books:
            shelf_info += str(book) + "\n"
        return shelf_info


class Library:
    def __init__(self):
        self.shelves = {}

    def add_shelf(self, code):
        if code not in self.shelves:
            self.shelves[code] = Shelf(code)

    def add_book(self, book, shelf_code):
        if shelf_code in self.shelves:
            self.shelves[shelf_code].add_book(book)

    def find_book(self, author, title):
        for shelf in self.shelves.values():
            for book in shelf.books:
                if book.get_author() == author and book.get_title() == title:
                    return shelf.code
        return None

    def get_books_from_shelf(self, shelf_code):
        if shelf_code in self.shelves:
            return self.shelves[shelf_code].get_books()
        else:
            return "Shelf not found"


# Example usage:
library = Library()
library.add_shelf("C1")
library.add_book(Book("John Doe", "Python Basics"), "C1")
library.add_book(Book("Jane Smith", "Java for Beginners"), "C1")
print(library.get_books_from_shelf("C1"))
print(library.find_book("John Doe", "Python Basics"))