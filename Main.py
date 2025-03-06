class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello my name is {self.name}")

# Example usage
p1 = Person("John", 36)
p1.myfunc()
