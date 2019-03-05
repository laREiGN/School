#Inheritance
#Taking all attributes, methods and etc from another objec

#class Parent:
    #implementation
#class Child(Parent):
    #implementation

# We use super() to call methods from the parent classs.

### INHERITANCE
#   Part 1
#

print("PART 1")

# BASE CLASS
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:",self.name," age:", self.age)


p1 = Person("Rob", 30)
p1.display()
p2 = Person("Maria", 21)
p2.display()

# CHILD
class Student(Person):
    # note we didn't introduce any change
    pass

p3 = Student("Jos", 22)
p3.display()

# note: we overrided both the constructor and display method
class Employee(Person):
    def __init__(self,name,age,job):
        super().__init__(name,age)
        self.job = job

    def display(self):
        print(self.name, "(", self.age,"):",self.job)

p4 = Employee("Mark",35,"teacher")
p4.display()
p5 = Employee("Albert", 42, "manager")
p5.display()

print("EOF part 1")
print("-"*20)
