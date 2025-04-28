# # # try:
# # #     fileHandler=open(r"text.txt","r")
# # #     if fileHandler:
# # #         print("File found")
    
# # #     a = print(fileHandler.readlines())



# # # except FileNotFoundError:
# # #     print("File not found ")

# # # fileHandler=open("text.txt")
# # # for line in fileHandler:
# # #     print(line)

# # file = open("text.txt","a")
# # # n = file.write("Hello")
# # # print(n)

# # # for i in range(5):
# # #     file.wti

# # list1=["Hello\n","Hi"]
# # file.writelines(list1)
# # print(file)

# # fileHandler=open("text.txt","a")
# # fileHandler.write("\n Hello Again")

# # fileHandler1=open()

# # with open("text.txt","r") as f:
# #     print(f.readline())

# pasth1=r"text.txt"
# pasth2=r"text2.txt"
# # with open(pasth1,"r") as inFile,open(pasth2,"w") as outFile:
# #     content=inFile.read()
# #     print(content)



# # def readFromFile(path):    
# #    with open(path,"r") as f:
# #         return f.read()
    
# # def replace(path,oldText,newText):
# #     with open(path,"r") as f:
# #        data=f.read()
# #        data = data.replace(oldText,newText)
# #     with open(path,"w") as f:
# #         f.write(data)

# # # myFile="text/task.txt"
# # # print("Original Text")
# # # readFromFile(myFile)
# # # print("After Replacement")
# # # replaceTextInFile(myFile,"Python")

# # def wordCount(path):
# #     count=0
# #     with open(path,"r") as f:
# #         data=f.read()
# #         lines=data.split()
# #         for word in lines:
# #             if not word.isnumeric():
# #                 count+=1
# #     return count

# # myFile="task.txt"
# # readFromFile(myFile)
# # print(wordCount(myFile))

# import string
# punctiations=string.punctuation
# print(punctiations)
# def remove(myText,marks):
#     resultString=""
#     for char in myText:
#         if char not in marks:
#             resultString+=char
#     return resultString
# def reverce(path):
#     with open(pasth1,"r") as f:
#         data=f.read()
#         data=remove(data,punctiations)
#         data=data.split()
#         data.reverse()
#         for word in data:
#             print(word)
# myFile="task.txt"
# reverce(myFile)


# def removeLine(fileIn,fukeOut,lineNo):
#     with open(fileIn,"r") as fr:
#         lines=fr.readlines()

#1
path= r"task1.txt"
def seven(myFile,wor,):
    with open(path,"r") as f:
        data=f.read()
    for wor in myFile:
        if len(wor)>=7:
            print(f"words: {wor}")

myFile="task1.txt"
wor = "task2.txt"
print(seven(myFile,wor))
#2
def r(path,oldText,newText):
    with open(path,"r") as f:
       data=f.read()
       data = data.replace(oldText,newText)
    with open(path,"w") as f:
       f.write(data)  
       
myFile2="task1"