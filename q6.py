import math
mylist=[]

string = input("please enter your numbers :")

# for i in range(len(string)):
#     if string[i] != ",":
#         mylist.append(string[i])
mylist = string.split(",")

for i in range(len(mylist)):
    print(int(math.sqrt(100*float(mylist[i])/30)))