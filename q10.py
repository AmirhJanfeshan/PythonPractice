mylist = []
words = input("enter your text: ")
mylist=words.split(" ")
myset = set(mylist)
mylist2 = list(myset)
mylist2.sort()

print("-----------------------------------")

for i in range(len(mylist2)):
    print(mylist2[i] , end=" ")

print()
print("-----------------------------------")
