# 1. Print your name
print("My name is Tony Stark")

# 2. Create 3 different type variables
name = "Tony"       # String
age = 42            # Integer
height = 1.85       # Float
is_student = True   # Boolean

# 3. Display variable types
print("\nVariable Types:")
print(type(name))       # str
print(type(age))        # int
print(type(height))     # float
print(type(is_student)) # bool

# 4. Check if number is 10
number = 10
if number == 10:
    print("\nTen")

# 5. Fruits list (3 items)
fruits = ["Apple", "Banana", "Cherry"]
print("\nSecond fruit:", fruits[1])  # Banana

# 6. Check if x equals 100
x = 100
print("\nIs x 100?")
print("Yes" if x == 100 else "No")  # Yes

# 7. Student dictionary
student = {
    "name": "Tony",
    "age": 42,
    "grade": "B"
}
print("\nStudent age:", student["age"])  # 22

# 8. Add grape to fruits
fruits.append("Grape")
print("\nUpdated fruits list:", fruits)  # ['Apple', 'Banana', 'Cherry', 'Grape']

# 9. Update student grade
student["grade"] = "A+"
print("\nUpdated student:")
print(student)  # {'name': 'Emily', 'age': 22, 'grade': 'A+'}

# 10. Person class
class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print(f"\nHello, {self.name}!")

# Create object and call method
person1 = Person("Tony")
person1.greet()  # Hello, John!
