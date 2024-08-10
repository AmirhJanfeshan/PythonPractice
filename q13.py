text = input("please Enter your text: ")
digits=0
alphaB=0

for i in range(len(text)):
    if text[i].isdigit():
        digits += 1
    elif text[i].isalpha():
        alphaB += 1
    
print(f"your text included {digits} Digits and {alphaB} Alphabetics")