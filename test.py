class Test:
    def __init__(self, name,age):
        print("Hello")
        self.age = age
        self.name = name
    def display(self):
        print(f"Hello world {self.age}")
        print(f"Hello world {self.name}")
T = Test("vath", 22)
T.display()