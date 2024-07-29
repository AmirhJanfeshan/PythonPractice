x=int(input("Enter your first number: "))
y=int(input("Enter your second number: "))

FinalList=[]

for i in range(x):
    innerList=[]
    for j in range(y):
        innerList.append(i*j)
    
    FinalList.append(innerList)

for i in range(x):
    print(FinalList[i])
    print()





