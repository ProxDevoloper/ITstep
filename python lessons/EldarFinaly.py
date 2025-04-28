# import random
# class Person:
#     def init(self, firstname,lastname, age):
#         self.firstname = firstname
#         self.lastname = lastname
#         self._age = age
#         self.__personId=10

#     def __showId(self):
#         print(self.__personId)

#     def showId(self):
#         return self.__personId

#     def setId(self,newId):
#         self.__personId=newId

#     def getInfo(self):
#         return f"{self.firstname} {self.lastname} {self._age} years old"

#     def getHi(self,msgText):
#         return f"{msgText} from {self.firstname} {self.lastname}"

# jake=Person("Jake","Jamesson",19)
# print(jake.firstname)
# print(jake.showId())

# jake.setId(15)
# print(jake.showId())

# # print(jake.__personId)
# # print(jake.__showId())

# class Employee(Person):
#     def init(self, firstname, lastname, age, salary):
#         super().init(firstname,lastname,age)
#         self.salary = salary

#     def isOld(self):
#         if self._age>40:
#             print("Old Employee")
#         else:
#             print("Young Employee")

# bob = Employee("Bob", "Smith", 40, 20000)
# # print(bob.__showId())
# # print(bob.__personId)
# bob.isOld()
# print(bob.showId())
# bob.setId(15)
# print(bob.showId())




# class myOPerator:
#     @staticmethod
#     def increment(str):
#         numbers= list(map(float,split()))

# def setBasicSalary(self):
#     if self._jobTitle=="Manager":
#         self._salary=10000

#     elif self.jobTitle=="Middle":
#         self._salary=5000
#     elif self.jobTitle=="Junior":
#         self._salary=2000
#     else:
#         self._salary=0


# useStr="1.5 5.6 4.7 9.0

# @staticmethod
# def printHi():                     
#     print("Hi i am Developer class")


# def getInfo(self):
#     print(f"{self.spec} {self._jobTitle} {self._salary} {self._age} years old")






# anuar = Developer("Anuar", "Aitbayev", 20, 2000, "Python", "Junior")
# anuar.setBasicSalary()
# anuar.getInfo()


# anuar.setRung("Middle")
# anuar.setBasicSalary()
# Developer.setspec("Java")


# class myBook:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages


#     def showBookInfo(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Pages: {self.pages}")

# class myFile:
#     def __init__(self,fileSize,scr):
#         self.fileSize=fileSize
#         self.scr=scr

#     def showFileInfo(self):
#         print(f"File Size: {self.fileSize}")
#         print(f"File Source: {self.scr}")








#     class myEBook(myBook,myFile):
#        def __init__(self, title, author, pages, fileSize, scr):
#             myBook.__init__(self, title, author, pages)
#             myFile.__init__(self,fileSize,scr)

# python = myEBook("Python", "Guido van Rossum", 300, 2.5, "www.python.org","/python/")
# python.showBookInfo()
# print(myEBook.mro())

# class myClass1:
#     def sayHi(self):
#         print("Hello from myClass1")

# class myClass2(myClass1):
#     def sayHi(self):
#         print("Hello from myClass2")

# class myClass3(myClass1):
#     def sayHi(self):
#         print("Hello from myClass3")

# class myClass4(myClass3, myClass2):
#     pass



# class Human:
#     count = 0
#     def __init__(self, name, age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.counter()

    
    

#         @staticmethod
#         def counter(self):
#             Human.count += 1
          
    
# bob = Human("Bob",23,"Male")
# print(Human.counter())
# print(bob.count)


#2 Задание
class Calculating_the_area_of_geometric_figures:
    
    @staticmethod
    def counter(self):
        Calculating_the_area_of_geometric_figures.count += 1

    @staticmethod
    def rectangle(width, height):
        return width * height

    @staticmethod
    def square(side):
        return side * side

    @staticmethod
    def triangle(base, height):
       return 0.5 * base * height


print(Calculating_the_area_of_geometric_figures.rectangle(5, 10))  
print(Calculating_the_area_of_geometric_figures.square(4))         
print(Calculating_the_area_of_geometric_figures.triangle(6, 3))   




# 3 Задание
