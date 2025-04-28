from functools import reduce

# def multiply_text(mystr,n):
#     return mystr*n
# print(multiply_text("Python",3))

# double_text=partial(multiply_text,n=5)
# triple_text=partial(multiply_text,n=3)
# print(double_text("Python"))
# print(triple_text("Python"))

# def calculator(a,b,c):
#     return a+b*c
# result = partial(calculator,c=10)
# print(result(1,2))

# @lru_cache
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# list1=[1,2,3,4,5]
# # def Mysum(x,y):
# #     return x+y

# # result1=reduce(Mysum,list1)
# # print(result1)
# pl = reduce(lambda x,y: x+y,list1)  
# print(pl)

# words=["Python","is","cool"]

# sentence = reduce(lambda x,y:x+" "+y,words)
# print(sentence)

# #1
# list1= [1,2,3,4,5]

# string = reduce(lambda x,y: str(x) + "-"+str(y),list1)
# print(string)

# #2
# plus = reduce(lambda x,y: x*y,list1)
# print(plus)

# def sumpleDecorator(myFunc):
#     def simplleWrapper():
#         print("Function starts working...")
#         myFunc()
#         print ("See you!")
#     return simplleWrapper

# def sumpleDecorator_v2(myFunc):
#     def simplleWrapper():
#         print("Let's start to work...")
#         myFunc()
#         print ("Good luck...:)")
#     return simplleWrapper
    
# @sumpleDecorator
# @sumpleDecorator_v2
# def say_hello():
#         print("Hello world!")

# say_hello()

# def decorator_v3(arg1,arg2):
#      def wraper1(myFunc):
#           def wraper2():
#                 print("Function starts working../")
#                 print(f"arg1: {arg1}, arg2 {arg2}")
#                 myFunc(*args,**kwargs)
#                 print("See you:")
#                 return wraper2
#      return wraper1
# @decorator_v3("I am", "Decorator")
# def say_hello_v2(name):
#      print(f"Hello {name}")
# say_hello_v2("Artem")

# def print_name(*args):
#     for name in args:
#         print(name)

# print_name("Kirill",7,"Anuar","ramzat",1,2,3,4,5,6,5,2,2,1,234,34,34,)

# def print_names_v2(**kwargs):
#     for name,age in kwargs.items():
#         print(f"{name} is {age} years old")

# print_names_v2(name1="Kirill",name2="Anuar",name3="Ramzat")
# list1=[1,"wad", 2,3]
# tuple1=(1,2,3)
# print(type(list1))
# print(type(tuple1))


# tuple2=1,2,3
# print(tuple2)
# lis1 = list(tuple2)
# lis1.append(4)
# print(lis1)

# tuple2=("admin","not admin")
# user1,user2=tuple2
# user10, *users=tuple2

# print(users)
# for i in tuple2:
#     print(i)

# if "not admin" in tuple2:
#     print("Yes")

cart = ("Ананас","банан","виноград")

list1= list(cart)
a = input("Введи фрукт")
print(list1.count(a))

#2

#3
cars = ("Mersedec","Toyota")

lis = list(cars)



