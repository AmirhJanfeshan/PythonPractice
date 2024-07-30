BNumbers = input("enter your binary numbers separated with ',' character: ")

BList = []
numberList =[]
final = []
BList = BNumbers.split(",")

for i in range(len(BList)):
    numberList.append(int(BList[i],2))

for i in range(len(BList)):
    if (numberList[i]%5) == 0:
        final.append(BList[i])
    
for i in range(len(final)):

    if i == (len(final) -1):
        print(final[i])
        break

    print(final[i] , end=" , ")

# print()