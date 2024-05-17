
# class ichimlik:
#     def __init__(self, nomi, narxi) :
#         self.__nomi = nomi
#         self.__narxi = narxi

#     def getNomi(self):
#       return self. __nomi

#     def getNarxi(self):
#        return self.__narxi

#     def setNomi(self, nom):
#         self.__nomi = nom

#     def setNarxi(self, narx):
#         self.__narxi = narx



# s = ichimlik("cola", 5000 )
# print(s.getNarxi())


"""ota boladan super klass olishi"""

# class Parent:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

        
#     def getname(self):
#       return self. name

#     def getage(self):
#        return self.age

#     def setage(self, name):
#         self.name =name

#     def setage(self, age):
#         self.age=age




#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
        
#     def salom(self):
#         print(f"salom {self.name}")



# class Child(Parent):
#     def __init__(self, name, age, school):
#         super().__init__(name, age)
#         self.school = school
    
#     def display(self):
#         super().display()
#         print("School:", self.school)

# # Test
# parent = Parent("John", 40)
# print("Parent Information:")
# parent.display()
# parent.salom()

# print("\n")

# child = Child("Alice", 10, "XYZ School")
# print("Child Information:")
# child.display()
# child.salom()

# print(child.getname())
# print(parent.getage())












