text = input("please enter your text: ")
upperNumber = 0
lowerNumber = 0

for i in range(len(text)):
    if text[i].isupper():
        upperNumber += 1
    elif text[i].islower():
        lowerNumber += 1

print(f"Number of Lower and Upper Case in text is : '{lowerNumber}' and '{upperNumber}'")