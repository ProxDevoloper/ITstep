#  #1 Задание
# def kvadrat(numb):
#      numb = lambda x: x ** x 
#      return numb 
# numb = 4
# kvadrat(numb)
# # #2
# t = lambda x:x%2 == 0
# print(t)

# #3

# a = lambda x,y:  x + y
# x = 2
# y = 7
# print(a)
# #4


# a = {1,2,3,4,5,6,3,3,3,3,3}
# b = {"A", "B", 3,2,True}
# c={1,2,3,(1,2)}

# d = set((1,2,3))
# names = {"Bob","Kate","Kirill","Max","Bob",1,1,2,3.2}
# var={"b",2,"a",3.6,False,"q"}

# print(var)

# user_name=["Joe","Bob"]

# for i in set(user_name):
#     print(i)

# word=input("Ener word ")
# for i in set(word):
#     print(i)



# myset={1,2,3,4,5}
# myset.add(7)
# print(myset)
# myset.remove(2)

# student1={"Hanna","Joe","Kate"}
# student2={"Bob","Joe","Kate","Jack","Jane"}
# print(student1.union(student2))
# print(student2.difference(student2))
# print(student1 - student2)
# print(student1 & student2 )

# print(student2.union(student1))


# students={"Bob","Joe","Kate","Jack","Jane"}

# for index,item in enumerate(students):
#     print(f"Index: {index}, Item: {}")

# froz1 = frozenset({1,23,4,4,5,7,7})
# froz2 = frozenset({1,56,4,2,5,3,7})
# print(froz1)
# print(type(froz2))

# print(froz1&froz2)
# print(froz1 | froz2)
# print(froz1-froz2)

# word1=input("Enter word: ")
# word2=input("Enter  word: ")
# if set (word1) ==set(word2):
#     print("Anagrams")
# else:
#     print("Net")
#1 Задание
# city = {"Russia","Poland","Germany"}
# user = input(f"Есть список стран: {city},введи что хочешь сделать?")
# if user == "Добавить страну":
#     user2 = input("Страна: ")
#     city.add(user2)
# elif user == "Удалить страну":
#     dell = input("Название: ")
#     city.remove()

#2
# city_name1={"Almaty","Berlin","Moscow","Karaganda"}
# city_name2={"Astana","Karaganda","Vladevostok","Moscow"}
# print(city_name1&city_name2)
#3
city_name1={"Almaty","Berlin","Moscow","Karaganda"}
city_name2={"Astana","Karaganda","Vladevostok","Moscow"}
print(city_name1 - city_name2)
# #4
print(city_name2 - city_name1)
#5
citys = {city_name1 - city_name2}
print(citys.union(city_name2 | city_name1))