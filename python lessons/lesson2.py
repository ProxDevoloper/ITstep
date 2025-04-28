import string
import random
import re
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)


# user_login="".join(random.sample(string.ascii_letters,6))
# password = "".join(random.sample(string.ascii_letters+string.digits+string.punctuation,52))
# print(user_login)
# print(password)



# word1="  @     Hello @      "
# word2="Hello,World,python"
# print(word1.strip(" @"))
# print(word2.split(","))

# t=string.Template("$name is a good man,i buy he")
# result=t.substitute(name="Kirill")
# print(result)

# name="Чипсы со сметаной"

# text="I have 3 apples and 2 oranges"
# pattern=r"\d"
# result=re.findall(pattern,text)
# print(result)


# text3="My emails: test@gmail.com,test2@gmail.com,work@mail.ru"
# pattern3=r"\w+@\w+.\w+"
# result3=re.findall(pattern3,text3)
# print(result3)


# text4="My number: 8823423"
# pattern4=r"\d"
# result4=re.sub(pattern4,"",text4)
# print(result4)

# text5="Today i was at school and i met Anna and Kolya"
# pattern5=r"\b[A-Z][a-z]+\b"
# result5=re.findall(pattern5,text5)





# word="hello"
# print(word.replace("hello","Python"))
# print(word[::-1])
# print(word.strip())

# try:
#  text = "привет меня зовут клавиатура!по мне каждый раз нажимают!я чёрная,так же я 1-дна на столе"
#  print(text.capitalize)



#  for i in text:
#     if i in string.digits:
#         count_digit+=1
#     if i in string.punctuation:
#         count_punct+=1
        
#  print(text.count("!"))

# except:
#  print("Ошибка")


# kolbaska=[1,2,3,4,5]
# print(kolbaska[1])

# list3=["HEllo","hi","world","python"]
# for i in list3:
#     print(i)
    
# for i in range(len(list3)):
#     print(list3[i])
# list4=["HEllo",3.5,"hi",[1,True,3],True,"world",20,"python"]
# print(list4[3][1])
# for i in list4:
#     if type(i)==list:
#         for j in i:
#             print(j)
#     print(j)

# word="Python"
# print(list(word)) 

# list5=[]
# for i in range(10):
#     list5.append(i*2)

# print(list5)

# word2="Hello"
# list6=[]
# for i in word2:
#     list6.append(i+'*')

# list7=[]
# for i in range(1,11):
#     if i%2!=0:
#         list7.append(i)
# print(list7)

# list8=[i*2 for i in range(1,11)]
# print(list8)

# list12=[input("numb") for i in range(1,11)]
# print(list12)

list=[input("Введите до пяти чисел: ")for i in range(1,5)]
da= int(input("Введи число"))


if da == list:

    print("Вот столько ваше число в списке:"+list)




#     if i in string.digits:
#         count_digit+=1