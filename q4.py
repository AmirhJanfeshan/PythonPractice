UserList = input("Enter your list: ")

numberList=[]

for i in range(len(UserList)):
    if UserList[i] != ",":
        numberList.append(UserList[i])


print(numberList)
print(tuple(numberList))