text = input("enter your sentence and use '\\n' instead of enter key(for the new line): ")

for i in range(len(text)):
    if text[i] == "\\" and text[i+1] == "n":
        print()
        continue
    if text[i] == "n" and text[i-1] == "\\":
        continue

    print(text[i].upper() , end="")
print()