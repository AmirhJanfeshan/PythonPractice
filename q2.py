num = int(input("Enter your number: "))
counter2 = 1

# for i in range(1,num+1):
#     counter *= i

while num > 0:
    counter2 *= num
    num -= 1

print(counter2)

# 5! = 5 * 4 * 3 * 2 * 1