class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def increase_age(self):
        self.age += 1

    def decrease_age(self):
        if self.age > 0:
            self.age -= 1  # break point here

    def __str__(self):
        return f"{self.name} is {self.age} years old."


person = Person("John", 5)
person.decrease_age()
person.decrease_age()
person.decrease_age()
person.decrease_age()
person.decrease_age()
person.decrease_age()
print(person)


class MyClass:
    def __init__(self):
        print("initialized")

    def printSomething(self):  # Define printSomething as a method
        print("python")


myClass = MyClass()
myClass.printSomething()  # Now this should work without errors
