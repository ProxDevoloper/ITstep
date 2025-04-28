# def add10(x):
#     return x * 15000
# my_numbers=[2,5,7,2.10,7.8]
# newNum=lambda x:x+10
# for i in my_numbers:
#     print(add10(i))
# 
# students=[['Bob',70],['Jane',80],['Andy',50]]
# print(students[1][1])
# print(students)
# sorted_students=sorted(students,key=lambda x: x[1])
# print(sorted_students) 

# tengeToDollar = 500
# discount=0.15
# priceDol=lambda x: x/tengeToDollar*(1-discount)
# def priceDolFunction(price):
#     return price/tengeToDollar*(1-discount)

# price=float(input("enter price"))
# print(f"price: {priceDol(price)}")

# username=lambda firstname,surname:f"{firstname.capitalize()} {surname.title()}"
# first_name =input("enter your first name")
# surn_name=input("enter surname: ")
# print(username(first_name,surn_name))
# print((lambda firstname,surname:f"{firstname.capitalize()} {surname.title()}")(first_name,surn_name))

# def nameUpper(name):
#     return "user " +name.upper()

# def nameLower(name):
#     return "user: "+name.lower()

# def make(username,maker):
#     return maker(username)
# user=input("enter username: ")
# userAnswer=input("upper 1 or lower 2:")
# if userAnswer=="1":
#     print(make(user,nameUpper))
# elif userAnswer=="2":
#     print(make(user,nameLower))

# userlog=["Admin","student","teacher","user"]
# userLogLower=list(map(str.lower(),userlog))

# values=["5.1","4.7","0.6","8.9"]
# valuesFloat=list(map(float,values))
# print(valuesFloat)
# firsNumber=list(map(lambda x: int(x[0]),values))
# print(firsNumber)
# pizza=["Chese","Pipironi","Double cheese","hawaii"]

# modpizza= lambda x:x + 'pizza'

# print(list(map(modpizza,pizza)))

# numberList1=[5,2,3]
# numberList2=[1,2,3]
# result=map(lambda x,y:x**y,numberList1,numberList2)

# prices=[100.45,8.56,234,15,87,567]
# expensive=list(filter(lambda x:x>10,prices))
# print(expensive)

# userLog=["user123","UserStudent","adminus","user-23"]
# def checkLogin(user):
#     if user.lower().find("user")!=-1:
#         return True
#     else:
#         return False
# selectedUser=list(filter(chekLogin,userLog))
# print(selectedUser)



# listLogin=["user123","UserStudent","adminus","user-23"]
# listPassword=["123","abcd","qwer","000"]
# listNames=["Artek","Anuar","Kirill","Ramzat"]
# for log,passw,name in zip(listLogin,listPassword,listNames):
#     print(f"login: {log} Password: {passw} Name{name}")

# list1=[1,2,3,4,5]
# list2=['a','b','c','d','v']
# list3=[True,False,True,False,True]
# print(zip(list1,list2))
# print(type(zip(list1,list2)))
# print(list(zip(list1,list2,list3)))

# def sayUserHello(user):
#     msg="Hello"+user
#     def showMsg():
#         print(msg+"!Let's start learning Python")
#     showMsg()
# sayUserHello("Kirill")

# def sayUserHello(user):
#      msg="Hello"+user
#      def showMsg():
#          print(msg+"!Let's start learning Python")
#      return showMsg

# sayUserHello("Kirill")

# def doExercies(var1):
#     var2=5
#     def doExrises2(var3):
#         return var1+var3
    
#     return doExrises2

# case1=doExercies(10)
# print(case1(5))
# print(case1(15))]]


def sendMsg(userTo):
   
    def setMsg(msgTxt):
        def setUserFrom(userFrom):
            def setLang(lang):
                print(f"Dear{userTo},"
                      f"Hello from {userFrom}"
                      f"Welcome to {lang} world,"
                      f"text: {msgTxt} ")

            return setLang
        return setUserFrom
    return setMsg

case1=sendMsg("admin")("Hello admin")
case1("teacher")("PyThOn")

# sendMsg("admin", "Hello admin")
# sendMsg("admin", "Hello admin")
# sendMsg("admin", "Hello admin")
# sendMsg("admin", "Hello admin")
# sendMsg("admin", "Hello admin")