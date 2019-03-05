class MyClass:   #Example slide 1
    x = 10

obj = MyClass()

print('\n'+'Example 1')
print(obj.x)
a = obj.x
obj.x += 5
print(a, obj.x)

obj1 = MyClass()   #Example slide 2
obj2 = MyClass()

obj1.x = 15
obj2.x -= 1

print('\n'+'Example 2')
print(obj1.x, obj2.x)

class Person:   #Example Slide 3
    age = 21
    name = 'John'

    def hello(self):
        print('\n'+'Example 4')
        print('Hello world!')

p1 = Person()
print('\n'+'Example 3')
print(p1.name, p1.age)

p2 = Person()
p2.name = 'Rob'
p2.age = 30
print(p2.name, p2.age)

p = Person()
p.hello()

class Person2:   #Example Slide 5
    age = 21
    name = 'John'
    def hello(self):
        print('\n'+'Example 5')
        print('Hello world!')
    def introduce(self):
        print('My name is ', self.name, 'and I am', self.age, ' years old')

p5 = Person2()
p5.hello()
p5.introduce()

class Person3:   #Example Slide 6
    age = 21
    name = 'John'
    def set_values(self, n, a):
        self.age = n
        self.name = a
    def get_age(self):
        return self.age
    def hello(self):
        print('\n'+'Example 5')
        print('Hello world!')
    def introduce(self):
        print('My name is ', self.name, 'and I am', self.age, ' years old')

p6 = Person3()
print('\n'+'Example 6')
print(p6.get_age())
p6.set_values(18, 'Girts')
p6.introduce()

class ConstructorPerson:   #Example slide 7
    age = None
    name = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print('My name is ', self.name, 'and I am', self.age, ' years old')

pCon = ConstructorPerson('Reign', 99)
print('\n'+'Example 7')
pCon.introduce()

class Test:    #Example slide 8
    b = None
    def __init__(self, val):
        a = val
        b = 2*val
        self.b = 3*val
        print('\n'+'Example 8')
        print(a, b, self.b)

t = Test(10)
# print(t.a, t.b)

class Car:    #Practice
    mark = 'Toyota'
    manufacturing_year = 1998
    color = 'blue'
    seat_number = 2

    def display_all(self):
        print(self.mark, self.manufacturing_year, self.color, self.seat_number)
    def car_age(self, manufacturing_year, current_year):
        age = current_year - manufacturing_year
        #print('This car is', age, 'years old.')
        return age
    def __init__(self, mark, manufacturing_year, color, seat_number):
        self.mark = mark
        self.manufacturing_year = manufacturing_year
        self.color = color
        self.seat_number = seat_number

c = Car('Toyota', 1998, 'Blue', 2)
print('\n'+'Practice')
c.display_all()
c.car_age(1998, 2018)
c1 = Car('BMW', 2016, 'Red', 4)
c1.display_all()
c1.car_age(2016, 2019)
