#App login
print("Registration,enter your password and login")
login = input("Enter your login")
try:
    password = int(input("Enter your password"))
except:
    print("Enter number,not string")

print("good!")
print("Login,enter your password and login")

login1 = input("Enter your login")
try:
    password1 = int(input("Enter your password"))
except:
    print("Enter number,not string")
    
if login == login1:
    print("Welcome!")

elif password == password1:
    print("Welcome!")

elif login != login1:
    print("No")

elif password != password1:
    print("No")
    