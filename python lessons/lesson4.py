import requests 
import math
import random

# x = int(input("Enter a number: "))
# if x<0:
#     x=abs(x)
# print(abs)

# print(math.sqrt(121))
# x=0.23
# y=1.67
# z=6

# print(math.ceil(x))
# print(math.floor(y))
# print(math.ceil(z))

# print(math.floor(x))
# print(math.floor(y))
# print(math.floor(z))

# print(math.modf(x))
# print(math.modf(y))
# print(math.modf(z))

# print(math.trunc(x))
# print(math.trunc(y))
# print(math.trunc(z))

# a=-1.5
# b=-5
# print(abs(a))
# print(abs(b))

# print(math.fabs(a))
# print(math.fabs(b))

# for i in range(3):
#     print(random.randint(1,10))
#     print(random.randint(1,10))
#     print(random.randint(1,10))

# for i in range(3):
#     print(random.randrange(1,10))
#     print(random.randrange(1,10))
#     print(random.randrange(1,10))

# list1=['a','b','c','d','e']
# print(random.choice(list1))

# list2=[random.randint(1,10) for i in range(10)]
# print(list2)


# def print_hello():
#     print("I don't love python")



# for i in range(5):
#     print(print_hello())


# x=int(input("Enter your number: "))
# y=int(input("Enter another number"))


# def add(x,y):
#     return x+y

# def add2(x,y):
#     return x+y

# result=add(x,y)
# print(result)



# def calculate(a,b,c):
#     print("Lets calculate")
#     print(a+b+c)
#     print(a-b-c)
#     print(a*b*b)


# x=5
# y=2
# z=4

# calculate(x,y,z)

# user=input("Enter your name: ")

# def mod_name(name):
#     newName=name.upper()
#     return newName

# newName=mod_name(user)
# print(newName)

# if mod_name(user).isupper():
#     print("Name is uppercase")
# else:
#     print("NAME IS LOWERCASE")
# student_list=['Eldar','Kirill','Erniyaz','Nurzhas']
# new_student="Maxim"
# def check_student(student):
#     if student in student_list:
#         return "Он в списке"
#     else:
#         return "Гитлера нет в списке!!!!"

# number1=int(input("Enter first number"))
# number2=int(input("Enter your second number"))
# def print_even(number)



# length=int(input("Enter your pength: "))
# choose-int(input("Choose: 1 - horisontal, 2 - vertivcal: "))
# symbol=input("Enter the symbol")
# def draw_line(lenght, choose,symbol):
#     if choose==1:
#         for i in range(lenght):
#             print(symbol,end="")
#     elif choose==2:
#         for i in range(lenght):
#             print(symbol)
#     else:
#         print("Wrong input")

#     draw_line(lenght,choose,symbol)
#1
def maxx():
    list1=[1,2,3,4]
    print(max(list1))


maxx()

#2
def func():

    try:
        summ=[int(input("Введи до 5 чисел: ")) for i in range(5)]
    except:
        print("Ошибка,нужно вводить только цифры")
    print(sum(summ))

#3
# def func2():
#     hogrider=int(input("Введи число: "))

    
#     while hogrider//2==hogrider and hogrider//hogrider==1:
#         print("TRUE(YES)")
#         break

#     while hogrider%2==0 or hogrider%2==0:
#         print("False(No(net))")
#         break
# func2()
#3 Задание
lucky=[int(input("Введи 6 чисел: "))for i in range(6)]
def luckynumb(lucky):
    print(sum(lucky[0:3]))
    print(sum(lucky(3:6)))

luckynumb(lucky)
