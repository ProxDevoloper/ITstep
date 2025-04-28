# # def checkStudentScore(score):
# #     if score >= 90:
# #         print("Excellent")
# #     elif score >= 65:
# #         print("Good")
# #     elif score >= 50:
# #         print("Normal")
# #     else:
# #         print("bad")

# # def checkStudentScore2(score):
# #     if score == 5:
# #         print("Excellent")
# #     elif score == 4:
# #         print("Good")
# #     elif score == 3:
# #         print("Normal")
# #     else:
# #         print("bad")
    
# # checkStudentScore(60)
# # checkStudentScore2(3)

# # userLogin = ["Admin", "User", "GoodStudent"]
# # usersYears=[2001,1995,2008]
# # def listMaker(myList):
# #     result = []
# #     for item in myList:
# #         result.append(item.lower())
# #     return result

# # def listMaker2(myList):
# #     result = []
# #     for item in myList:
# #         result.append(2025-item)
# #     return result

# # print(listMaker(userLogin))
# # print(listMaker2(usersYears))

# class Person:
#     # name="Bob"
#     # age=20
#     spec="I am a person"
#     def __init__(self, name="Bob", age=20):
#         self.name = name
#         self.age = age


#     def say_hello(sefl):
#         print(sefl.name,"says hello")



#     def walk(self):
#         print(self.name + "walks")


# mark = Person()
# mark.name = "Mark"
# print(mark.name)

# mark.say_hello()
# mark.walk()










# # bob = Person("Bob", 20)
# # kate = Person("Kate", 25)
# # print(bob.name)
# # print(kate.name)
# # print(bob.age)
# # print(kate.age)




# # bob = Person()
# # print(bob.name)
# # print(bob.age)

# # kate= Person()
# # print(kate.name)
# # print(kate.age)





# class Animal:
#     def __init__(self, name, age,type,color,weight):
#         self.color = color
#         self.name = name
#         self.age = age
#         self.type = type
#         self.weight = weight
    
#     def speak(self):
#         if self.type == "cat":
#             print("Meow")
#         elif self.type == "dog":
#             print("Woof")
#         elif self.type == "bird":
#             print("uuuuuu")
#         else:
#             print("Unknown animal sound")
        
#     def move(self):
#         if self.type == "cat":
#             print("Cat is walking")
#         elif self.type == "dog":
#             print("Dog is running")
#         elif self.type == "bird":
#             print("Bird is flying")
#         else:
#             print("Unknown animal movement")

# murzik= Animal("Murzik", 3, "cat", "black", 2)
# murzik.move()
# murzik.speak()


# rex = Animal("Rax", 5, "dog", "white", 35)
# rex.move()
# rex.speak()









# x= 10
# class Looker:
#     x = 15
#     print(x)
#     def func1(self):
#         x = 20
#         print(x)
#     def func2(self):
#             x =30
#             print(x)

# objc = Looker()
# objc.func1()

# import random


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.glandness = 50
#         self.progess = 0
#         self.money = 1000
#         self.satiety = 100
#         self.alive = True

#     def to_study(self):
#         print("Time to study")
#         self.progess += 0.3
#         self.glandness -= 5
#         self.satiety -= 2

#     def to_sleep(self):
#         print("Time to sleep")
#         self.glandness += 5
#         self.satiety -= 5

#     def to_chill(self):
#         print("Time to chill")
#         self.glandness += 5
#         self.progess -= 0.1
#         self.satiety -= 2

#     def to_eat(self):
#         print("Time to eat")
#         self.satiety += 10
#         self.glandness += 1
#         self.money -= 100

#     def to_shopping(self):
#         print("Time to shopping")
#         self.glandness += 5
#         self.progess -= 0.1
#         self.money -= 200

#     def to_work(self):
#         print("Time to work")
#         self.glandness -= 5
#         self.progess += 0.5
#         self.money += 500
#         self.satiety -= 2

#     def end_of_day(self):
#         print("End of day")
#         print(f"Progess: {self.progess}")
#         print(f"Glandness: {self.glandness}")
#         print(f"Money: {self.money}")
#         print(f"Satiety: {self.satiety}")
#         print(f"Alive: {self.alive}")

#     def check_alive(self):
#         if self.progess <= -5:
#             print("Ahhh.....")
#             self.alive = False
#         elif self.glandness <= 0:
#             print("Depression")
#             self.alive = False
#         elif self.satiety <= 0:
#             print("Fooood......")
#             self.alive = False
#         elif self.money <= 0:
#             print("No money")
#             self.alive = False
#         else:
#             print("Alive")
#             self.alive = True

#     def live(self, day):
#         day = f"Day {day} of {self.name} life"
#         print("...........................................................")
#         print(f"Live: {day}")
#         live_cube = random.randint(1, 7)
#         if live_cube == 1:
#             self.to_study()
#         elif live_cube == 2:
#             self.to_sleep()
#         elif live_cube == 3:
#             self.to_chill()
#         elif live_cube == 4:
#             self.to_eat()
#         elif live_cube == 5:
#             self.to_shopping()
#         elif live_cube == 6:
#             self.to_work()
#         self.end_of_day()
#         self.check_alive()


# bob = Student("Kirill")
# for day in range(366):
#     if not bob.alive:
#         break
#     bob.live(day)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_name(self,name):
#         self.name = name
    
#     def get_name(self):
#         return self.name

# bob = Person("Bob", 20)
# print(bob.get_name())
# bob.set_name("Alice")


#1 Задание

class Human:
    def __init__(self, name,date_of_birth,contact_number,city,country,home_adress):
        self.name = name
        self.date_of_birth = date_of_birth
        self.contact_number = contact_number
        self.city = city
        self.country = country
        self.home_adress = home_adress


    def get_name(self,name):
        self.name = name

    def get_name(self):
        return self.name
    
    def get_date_of_birth(self,date_of_birth):
        self.date_of_birth = date_of_birth

    def get_date_of_birth(self):
        return self.date_of_birth
    
    def get_contact_number(self,contact_number):
        self.contact_number = contact_number
    
    def get_contact_number(self):
        return self.contact_number
    
    def get_city(self,city):
        self.city = city

    def get_city(self):
        return self.city
    
    def get_country(self,country):
        self.country = country

    def get_country(self):
        return self.country
    
    def get_home_adress(self,home_adress):
        self.home_adress = home_adress
    
    def get_home_adress(self):
        return self.home_adress
    


Human = Human("Eldar", "2007-01-01", "+380123456789", "Almaty", "Kazahstan", "Abaya 23")
Human.get_city
Human.get_country
Human.get_home_adress
Human.get_name
Human.get_date_of_birth
print(Human.get_name())
print(Human.get_date_of_birth())
print(Human.get_contact_number())
print(Human.get_city())
print(Human.get_country())
print(Human.get_home_adress())
print(Human.get_name())



#2 Задание
class Town:
    def __init__(self, name_town,name_country,name_region,count):
        self.name_town = name_town
        self.name_country = name_country
        self.name_region = name_region
        self.count = count
    


    def get_name_town(self,name_town):
        self.name_town = name_town
    def get_name_town(self):
        return self.name_town
    
    def get_name_country(self,name_country):
        self.name_country = name_country

    def get_name_country(self):
        return self.name_country
    

    def get_name_region(self,name_region):
        self.name_region = name_region

    def get_name_region(self):
        return self.name_region
    

    def get_count(self,count):
        self.count = count
    
    def get_count(self):
        return self.count
    
    
Town= Town("Almaty", "Kazahstan", "Almaty", 2000000)
Town.get_name_town
Town.get_name_country
Town.get_name_region
Town.get_count
print(Town.get_name_town())
print(Town.get_name_country())
print(Town.get_name_region())
print(Town.get_count())
print(Town.get_name_town())
print(Town.get_name_country())





#3 Задание

class Country:
#     def __init__(self, name_country, name_continent, count_people,number_code,name_capital,name_towns):
#         self.name_country = name_country
#         self.name_continent = name_continent
#         self.count_people = count_people
#         self.number_code = number_code
#         self.name_capital = name_capital
#         self.name_towns = name_towns

#     def get_name_country(self,name_country):
#         self.name_country = name_country

#     def get_name_country(self):
#         return self.name_country
    

#     def get_name_continent(self,name_continent):
#         self.name_continent = name_continent

#     def get_name_continent(self):
#         return self.name_continent
    
#     def get_count_people(self,count_people):
#         self.count_people = count_people

#     def count_people(self):
#         return self.count_people
    
#     def get_number_code(self,number_code):
#         self.number_code = number_code

#     def get_number_code(self):
#         return self.number_code
    
#     def get_name_capital(self,name_capital):
#         self.name_capital = name_capital

#     def get_name_capital(self):
#         return self.name_capital
    
#     def get_name_towns(self,name_towns):
#         self.name_towns = name_towns

#     def get_name_towns(self):
#         return self.name_towns
    
# Russia = Country("Russia", "Eurasia", 146000000, 7, "Moscow", "Saint-Petersburg")
# Russia.get_name_country
# Russia.get_name_continent
# Russia.get_count_people
# Russia.get_number_code
# Russia.get_name_capital
# Russia.get_name_towns
# print(Russia.get_name_country())
# print(Russia.get_name_continent())
# print(Russia.get_count_people())
# print(Russia.get_number_code())
# print(Russia.get_name_capital())
# print(Russia.get_name_towns())





#4 Задание

class Drob:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def get_numerator(self,numerator):
        self.numerator = numerator
    
    def get_numerator(self):
        return self.numerator
    
    def get_denominator(self,denominator):
        self.denominator = denominator

    def get_denominator(self):
        return self.denominator
    def calculator(user,a, b, operation):
        operation = input("Enter operation (+, -, *, /): ")
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            return "Invalid operation"

                                                
operation = Drob(1, 2)
operation.get_numerator
operation.get_denominator


