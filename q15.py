numbers=[]
total = 0

Fnumber=input("Enter your number: ")

for i in range(1, 5):
    temp=''
    for j in range(1 , i+1):
        temp += Fnumber
    numbers.append(temp)

for i in range(len(numbers)):
    total += int(numbers[i])

print(total)