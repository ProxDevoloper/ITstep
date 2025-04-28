# dicts={
#     "Username":"Bobik",
#     "password":"223222",
#     "email":3.14,
#     "bool":True,
#     1:"1",
#     3.14:"3.14"
# }
# mydict=dict([("a",1),("b",2),("c",3)])
# print(mydict)

# mydict2=dict([["a",1],["b",2],["c",3]])
# print(mydict2)

# mydict3=dict(["aw","asd","fddf"])

# keyList=["a","b","c"]
# valueList=[1,2,3]
# mydict=dict([("a",1),("b",2),("c",3)])
# print(mydict)



# mydict5=dict(a=1,b=2,c=3)
# print(mydict5)


# hash_table={
#     key1=str(hash("a"))
#     key2=str(hash("b"))
#     key3=str(hash("c"))

# hash_table={
#     key1:1,
#     key2:2,
#     key3:3
# }
# print(hash_table)
# print(len(hash_table))

# bookDict={
#     "author":"Eric Metthes",
#     "title":"Pytohn forest",
#     "price":2001,
#     "age":"123 years and up",
#     "language":"English"
# }
# infoType=input("What information do you"
#                "want to know about the book?")
# if infoType in bookDict:
#     print(bookDict[infoType])
# else:
# print("Sorry")


# for key in bookDict:
#     print(key,bookDict[key])
# print()
# bookDict["content"]="......."
# for key,valuse in bookDict.items():
#     print(key,value)


# empty_dict={}
# new_info=input("What key do you want to add? ")
# if new_info!="":
#     new_infoValue=input("What value do you want to add? ")

#     if new_infoValue!="":
#         empty_dict[new_info]=new_infoValue
#     else:
#         print("Sorrt")

# else:
#     print("Sorry")

# print(bookDict["price"])
# print(bookDict.get("price123",-1))
# bookDict.update([("desccr",123),("desccr",123),("desccr",123)])
# test_dict={1:1,2:2,3:3}
# bookDict.update(test_dict)
# print(bookDict)
# del bookDict["author"]
# print(bookDict)
# bookDict.clear()

# print(list(bookDict.keys()))
# print(list(bookDict.values()))
# print(list(bookDict.items()))
# del bookDict["descr"]
# new=bookDict.pop
# print(bookDict)




# test_dict1={1:1,2:2,3:3}
# test_dict2={4:4,5:5,6:6}

# test_dict1 = test_dict2
# print(test_dict1)


# test_dict1[1]=100
# test_dict2[1]=200
# print(test_dict1)
# print(test_dict2)



# users=[
#     {"name":"Hanna","age":23,"login":"user22"},
#     {"name":"Roma","age":18,"login":"user23"},
#     {"name":"Igor","age":34,"login":"us44"},
#     {"name":"Kate","age":21,"login":"user2"},
# ]
# keyName=input("Key? ")
# keyValue=input("Value? ")
# keyValue=keyValue if keyName!="age" else int(keyValue)
# isElemenFound=False

# for user in users:
#     if user.get(keyName)==keyValue:
#         print("Element found!")
#         for key in user.items():
#             print(key,value)
#         isElemenFound=True
#         break
# if not isElemenFound:
#     print("Elent not found")



# filmDict={
#     "title":"Интерстеллар",
#     "creator":"Кристофер Нолан",
#     "genre":"Научная фантастика|приключения",
#     "year":2014,
#     "rating":8.7,
# }

# sortedTup=sorted(filmDict.items(),key=lambda x:x[0])
# print(sortedTup)
# filmDict2=dict(sortedTup)
# print(filmDict2)


# keyList=list(filmDict.keys())
# print(keyList)


users=[
    {"name":"Hanna","age":23,"login":"user22"},
    {"name":"Roma","age":18,"login":"user23"},
    {"name":"Igor","age":34,"login":"us44"},
    {"name":"Kate","age":21,"login":"user2"},
]
# sortedUsers=sorted(users,key=lambda x:x["name"])
# for user in sortedUsers:
#     for key,value in user.items():
#         print(key,value)


# users15=list(filter(lambda x:x["age"]>15,users))
# for user in userAge:
#     for key,value in user.items():
#         print(key,value)
phonebook={
    "Rick":"103",
    "Morty":"123",
    "Bob":"145",
    "Dipper":"232"
}

keyName= input("Name? ")
number = input("Numb? ")
isElemenFound=False

for keyName in phonebook:
    if phonebook.get(keyName)==number:
        print("Number found!")
        for key in phonebook.items():
            print(key)
        isElemenFound=True
    break
if not isElemenFound:
    print("Name not found")


new_info=input("What key do you want to add? ")
if new_info!="":
    new_infoValue=input("What value do you want to add? ")

    if new_infoValue!="":
        phonebook[new_info]=new_infoValue
    else:
        print("Sorry")

else:
    print("Sorry")

#2

coundt = { 
        "Burger"
        "Kaban"
}
user= input("Введи строку текста")

