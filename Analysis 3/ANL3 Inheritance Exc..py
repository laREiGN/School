class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def getInfo(self):
        print('Name:', self.first_name, self.last_name)

p1 = Person('John', 'Smith')
p1.getInfo()

class Student(Person):
    def __init__(self, first_name, last_name, std_num):
        super().__init__(first_name, last_name)
        self.std_num = std_num
    def getInfo(self):
        print('Name:', self.first_name, self.last_name, ', Student Number: ', self.std_num)

s1 = Student('John', 'Smith', 1234)
s1.getInfo()

class BachelorStudent(Student):
    study_duration = 4
    def __init__(self, first_name, last_name, std_num):
        super().__init__(first_name, last_name, std_num)
    def getInfo(self):
        print('Name:', self.first_name, self.last_name, ', Student Number:', self.std_num, ', Studies', self.study_duration, 'hours a day')

bs1 = BachelorStudent('John', 'Smith', 12340)
bs1.getInfo()

class MasterStudent(Student):
    study_duration = 2
    def __init__(self, first_name, last_name, std_num):
        super().__init__(first_name, last_name, std_num)
    def getInfo(self):
        print('Name:', self.first_name, self.last_name, ', Student Number:', self.std_num, ', Studies', self.study_duration, 'hours a day')

ms1 = MasterStudent('John', 'Smith', 123400)
ms1.getInfo()
