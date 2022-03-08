class Schoolmember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized Schoolmember: {}'.format(self.name))

    # def detail(self):a

class Teacher(Schoolmember):
    def __init__(self, name, age, salary):
        Schoolmember.__init__(self, name, age)
        self.salary = salary
        print('Initialized Teacher: {}'.format(self.name))

    def detail(self):
        print('Name: {}, Age: {}, Salary: {}'.format(self.name, self.age, self.salary))

class Student(Schoolmember):
    def __init__(self, name, age, mark):
        Schoolmember.__init__(self, name, age)
        self.mark = mark
        print('Initialized student: {}'.format(self.name))

    def detail(self):
        print('Name: {}, Age: {}, Mark: {}'.format(self.name, self.age, self.mark))


teacher = Teacher('Mrs.Alake', age = 27, salary = 1000)
student = Student('Kartone', 18, 4.6)

print()

members = [teacher, student]
for member in members:
    member.detail()

