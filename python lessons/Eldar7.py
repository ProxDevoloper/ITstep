# class Person:
#     def __init__(self, firstname,lastname, age):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age

#     def get_info(self):
#         return f"{self.firstname} {self.lastname} {self.age} years old."

#     def get_hi(self,msgText):
#         return f"{msgText}! I am {self.firstname}"


# bob = Person("Bob", "Smith", 25)
# kate = Person("Kate", "Johnson", 30)
# print(bob.get_info())
# print(kate.get_info())
# print(bob.get_hi("Hello Bob!"))
# print(kate.get_hi("Hello Kate!"))


# class Student(Person):
#     spec="Computer Science"
#     def __init__(self, firstname, lastname, age,score):
#         super().__init__(firstname, lastname, age)
#         self.score = score

#     def isSuccessful(self):
#         return True if self.score >= 60 else False



#     def get_info(self):
#         return super().get_info() + f"score: {self.score}"

# kirill = Student("Kirill", "Hovin", 15,76)
# print(kirill.get_info())
# print(f"Result: {kirill.isSuccessful()}")



# class Employee(Person):
#     def __init__(self, firstname, lastname, age, salary,job,level):
#         super().__init__(firstname, lastname, age)
#         self.job = job
#         self.level = level
#         self.salary = salary

#     def get_info(self):
#         return (super().get_info() +
#          f" salary: {self.salary} "
#          f"job: {self.job} "
#          f"level: {self.level}")



#     def check_level(self):
#         if self.level >=7:
#             print("Senior")
#         elif self.level > 3 and self.level < 7:
#             print("Middle")


#         else:
#             print("Junior")



# dias = Employee("Dias", "Kairbekov", 25, 1000, "Python Developer", 6 and 7)
# print(dias.get_info())
# dias.check_level()


# import random
#
# auto_list = {
#         "BMW": {"fuel": 100,"strength": 100,"consumption": 10},
#         "Mercedes": {"fuel": 150,"strength": 40,"consumption": 20},
#         "Lexus": {"fuel": 200,"strength": 50,"consumption": 30},
#         "Toyota": {"fuel": 60,"strength": 60,"consumption": 40},
#
#     }
# job_list = {
#     "Java Developer":{"salary": 150,"gladness_less":10},
#     "Python Developer":{"salary": 200,"gladness_less":5},
#     "C++ Developer":{"salary": 250,"gladness_less":2},
#     "JavaScript Developer":{"salary": 300,"gladness_less":1},
# }
#
# class Auto:
#
#
#     def __init__(self,auto_list):
#         self.brand= random.choice(list(auto_list))
#         self.fuel=auto_list[self.brand]["fuel"]
#         self.strength=auto_list[self.brand]["strength"]
#         self.consumption=auto_list[self.brand]["consumption"]
#
#     def drive(self):
#         if self.strength > 0 and self.fuel > self.consumption:
#             self.fuel -= self.consumption
#             self.strength -= 1
#             return True
#         else:
#             print("You can't drive")
#             return False
#
#
#
#
# class Job:
#     def __init__(self,job_list):
#         self.job = random.choice(list(job_list))
#         self.salary = job_list[self.job]["salary"]
#         self.gladness_less = job_list[self.job]["gladness_less"]
#
#
#
# class House:
#     def __init__(self):
#         self.mess=0
#         self.food=0
#         self.clean=0
#
#
#
#
#
# class Player(Auto,Job,House):
#     def __init__(self,name,job_list,auto_list):
#         Auto.__init__(self,auto_list)
#         Job.__init__(self,job_list)
#         House.__init__(self)
#         self.name=name
#         self.gladness=50
#         self.progress = 0
#         self.money = 1000
#         self.satiety=100
#         self.is_alive=True
#
#     def to_study(self):
#         print("Time to study")
#         self.progress+=0.3
#         self.gladness-=5
#         self.satiety-=2
#
#     def to_sleep(self):
#         print("Time to sleep")
#         self.gladness+=3
#         self.satiety -= 5
#         self.mess+=0.5
#     def to_relax(self):
#         print("Time to relax")
#         self.progress-=0.3
#         self.gladness+=5
#         self.satiety-=2
#         self.mess+=1
#
#     def to_eat(self):
#         print("Time to eat")
#         self.satiety+=5
#         self.gladness+=1
#         self.money-=50
#
#     def to_shopping(self):
#         print("Time to shopping")
#         self.gladness+=2
#         self.satiety-=2
#         self.money-=300
#
#     def to_work(self):
#         if self.to_work:
#             print("Time to work")
#             self.gladness-= self.gladness_less
#             self.progress+=0.5
#             self.money+= self.salary
#             self.satiety -= 3
#             self.mess += 2
#         else:
#             self.progress-= 0.5
#             print("Car is broken")
#
#
#
#     def to_repair(self):
#         print("Time to repair")
#         self.money-= 300
#         self.strength+=20
#
#     def to_fuel(self):
#         print("Time to fuel")
#         self.money-= 150
#         self.fuel+=50
#
#     def clean(self):
#         print("Time to clean")
#         self.mess -= 5
#
#
#     def to_buy_food(self):
#         print("Time to buy food")
#         self.money -= 100
#         self.food += 100
#
#
#
#     def end_of_day(self):
#         print("Time to end of day")
#         print(f"Gladness: {self.gladness}")
#         print(f"money: {self.money}")
#         print(f"Satiety: {self.satiety}")
#         print(f"progress: {self.progress}")
#         print(f"Mess: {self.mess}")
#         print(f"Clean: {self.clean}")
#         print(f"Car: {self.brand}")
#         print(f"Fuel: {self.fuel}")
#         print(f"Strength: {self.strength}")
#         print(f"Auto: {self.brand}")
#         print(f"Job: {self.job}")
#         print("food: ", self.food)
#
#
#     def alive(self):
#         if self.progress<=-0.5:
#             print("AAAHHH.....")
#             self.is_alive=False
#         elif self.gladness<=0:
#             print("Depression")
#             self.is_alive = False
#         elif self.satiety<=0:
#             print("Fooooooood,")
#             self.is_alive = False
#         elif self.money<=0:
#             print("You are broke")
#             self.is_alive = False
#
#
#         elif self.fuel<=0:
#             self.to_fuel()
#
#         elif self.strength<=0:
#             print("Car is broken")
#             self.to_repair()
#
#     def live(self,day):
#         day=f"Day {day} of {self.name} life"
#         print("---------------------------------------------------------")
#         print(f"Live: {day}")
#         live_cube=random.randint(1,7)
#         if live_cube==1:
#             self.to_study()
#         elif live_cube==2:
#             self.to_sleep()
#         elif live_cube==3:
#             self.to_relax()
#         elif live_cube==4:
#             self.to_eat()
#         elif live_cube==5:
#             self.to_shopping()
#         elif live_cube==6:
#             self.to_work()
#         self.end_of_day()
#         self.alive()
#
# bob=Player("Bob",job_list,auto_list)
# for day in range(366):
#     if bob.is_alive==False:
#         break
#     bob.live(day)
#
#



class Animal:
    def __init__(self, name,color,pawses, tail,size,sound,food):
        self.name = name
        self.color = color
        self.pawses = pawses
        self.tail = tail
        self.size = size
        self.sound = sound
        self.is_alive = True


class Tiger(Animal):
    def __init__(self, name, color, pawses, tail, size, sound, food):
        super().__init__(name, color, pawses, tail, size, sound,food)
        self.is_alive = True

    def roar(self,sound):
        self.sound = print(f"{self.name} {self.sound}")
        

    

    def eat(self,food):
        print("Tiger eat")
        


    def hunter(self,food):
        print("Tiger is hunting")
        

class Crocodile(Animal):
    def __init__(self, name, color, pawses, tail, size, sound, food):
        super().__init__(name, color, pawses, tail, size, sound,food)
        self.is_alive = True

    def roar(self,sound):
        self.sound = print(f"{self.name} {self.sound}")
        

    def eat(self,food):
        print("Crocodile eat")
        


    def hunter(self,food):
        print("Crocodile is hunting")



    def swiming(self):
        print("Crocodile is swimming")


class Kangaroo(Animal):
    def __init__(self, name, color, pawses, tail, size, sound, food):
        super().__init__(name, color, pawses, tail, size, sound,food)
        self.is_alive = True

    def roar(self,sound):
        self.sound = print(f"{self.name} {self.sound}")
        

    def eat(self,food):
        print("Kangaroo eat")
        


    def hunter(self,food):
        print("Kangaroo is hunting")


    def jump(self):
        print("Kangaroo is jumping")


    def big_pocket(self):
        print("Kangaroo has a big pocket")



#2 задание


class Passport:
    def __init__(self, name, surname, age, passport_number,date_of_birth):
        self.name = name
        self.surname = surname
        self.age = age
        self.passport_number = passport_number
        self.date_of_birth = date_of_birth


class ForeignPassport(Passport):
    def __init__(self, name, surname, age, passport_number,date_of_birth,country,visas,number_of_ForeignPassport):
        super().__init__(name, surname, age, passport_number,date_of_birth)
        self.country = country
        self.visas = visas
        self.number_of_ForeignPassport = number_of_ForeignPassport


    
    



#1 задание
class Human:
    def __init__(self, name, surname, age,date_of_birth,passport_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.passport_number = passport_number
        self.date_of_birth = date_of_birth


class Builder(Human):
    def __init__(self, name, surname, age,date_of_birth,work_experience,salary,build):
        super().__init__(name, surname, age,date_of_birth)
        self.work_experience = work_experience
        self.salary = salary
        self.build = build


class Sailor(Human):
    def __init__(self, name, surname, age,date_of_birth,work_experience,salary,ship):
        super().__init__(name, surname, age,date_of_birth)
        self.work_experience = work_experience
        self.salary = salary
        self.ship = ship


        
class Pilot(Human):
    def __init__(self, name, surname, age,date_of_birth,work_experience,salary,airplane,experience_of_plane):
        super().__init__(name, surname, age,date_of_birth)
        self.work_experience = work_experience
        self.salary = salary
        self.airplane = airplane
        self.experience_of_plane = experience_of_plane

    
    