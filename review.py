# class Test:
#     def name(self):  # self is a variable that represent as abject that calling method
#         print("test lg")
        
# t = Test()
# t.name()


class Ttest:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("this is my age: ", self.age)
        print(f"this is my name: {self.name}")
   
        
        
# a = Ttest("ju", 20)
# t = Ttest("vath", 19)
name = input("Enter your name here: ")
age = input("Enter your age here: ")
t = Ttest(name, age)
t.input()
t.display()
