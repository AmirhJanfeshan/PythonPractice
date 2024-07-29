class My_Class:
    print("###this is beganing massage of My_Class###")

    def getString(self):
        UserString = input("please Enter your string: ")
        return UserString

    def PrintString(self):
        print(self.getString().upper())


o1 = My_Class()
o1.PrintString()