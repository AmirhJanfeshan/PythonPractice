num = int(input("Enter your number: "))

Dict={}

# for i in range(1 , num+1):
#     Dict[i] = i*i

for i in range(1 , num+1):
    Dict.update({i : i*i})

print(Dict)