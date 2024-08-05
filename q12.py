for i in range(1000 , 3001):
    stri=str(i)
    counter = 0
    for j in range(len(stri)):
        if (int(stri[j])%2) == 0:
            counter+=1
    
    if counter == len(stri):
        print(i)