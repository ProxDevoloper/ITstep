class Film:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

    def showInfo(self):
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Genre: {self.genre}")
    

class Book:
    def __init__(self, title, author, pages,feedback):
       
        self.title = title
        self.author = author
        self.pages = pages
        self.feedback = feedback


    def __add__(self,other):
        return self.pages + other.pages
    
    def __sub__(self,other):
        return self.pages - other.pages
    
    def mul(self,other):
        return self.pages * other.pages
    
    def __truediv__(self,other):
        if other.pages != 1:
            raise ZeroDivisionError("You can't divide by 0")
        else:
            return self.pages / other.pages


    def __str__(self):
        return f"Hi am book object: self.title {self.title}"


    def __eq__(self,other):
        if self.title==other.title and self.pages==other.pages:
            return True
        else:
            return False
        

    def __ge__(self,other):
        if self.pages >= other.pages:
            return True
        else:
            return False
        
    def __gt__(self,other):
        if self.pages > other.pages:
            return True
        else:
            return False
        

    def __le__(self,other):
        if self.pages <= other.pages:
            return True
        else:
            return False
        
        
    def __lt__(self,other):
        if self.pages < other.pages:
            return True
        else:
            return False
        

    def __ne__(self,other):
        if self.pages != other.pages:
            return True
        else:
            return False

    def __getitem__(self, index):
        if 0 <= index <= 11:
            return self.feedback[index]
        else:
            return - 1


    def showInfo(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


# minecraft = Film("Minecraft", "fantasy", 2025)
# python = Book("Python", "Science", 300,[1,8,10,4,7,5,6,8,3,4,5,7])
# c=Book("C++", "Science", 300,[4,8,5,1,1,9,1,8,3,4,2,3])

# print(python==c)
# print(python!=c)
# print(python>=c)
# print(python<=c)
# print(python>c)
# print(python<c)
# print(python[2])
# print(python+python)
# print(python+c)
# print(python-c)          
# print(python.mul(c))
# print(python/c)








class Class1:
    def __new__(cls):
        print("Hi, I am __new__ magic method")
        return super(Class1, cls).__new__(cls)


    def __init__(self):

        print("Hi, I am __init__ magic method")




def doExercise1(var1):
    def doExercise2(var2):
        return var1 ** var2
    return doExercise2


case1=doExercise1(2)
print(case1(3))
print(case1(4))

class UserPlayer:
    def __init__(self, name):
        self.name = name
        self.__wallet = 100

    def updateWallet(self, amount):
        self.__wallet += amount

    def showWallet(self):
        print(f"Wallet: {self.__wallet}")


user1= UserPlayer("Me")
user1.updateWallet(100)
user1.showWallet()







class WalletFunctor:
    def __init__(self, startCoins=100):
        self.coins = startCoins

    def addCoins(self, amount):
        self.coins += amount

    def showCoins(self):
        print(f"Coins: {self.coins}")


priceUSD=[100,34,6,2,7]
USDrate=513


def changePriceDecorator(func):
    print("Code Before Wrapper")
    def simpleWrapper(argList):
        print("Code Before Function")
        result=func(argList)
        result= list(map(lambda x: x*(1-0.15), result))
        print("Code After Function")
        return result

        return simpleWrapper
@changePriceDecorator
def toPriceNew(priceList):
    return list(map(lambda x: x*USDrate, priceList))

def methodDecorator(func):
    def wrapper(self):
        print("General information")
        func(self)
    return wrapper



class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def showInfo(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

book = Book("Python", "John Doe", 300)
book.showInfo()

@myDecorator
def addNums(x, y):
    return x + y

addNums(2,3)
addNums(2,4)
addNums(4,3)
addNums.showMemory()