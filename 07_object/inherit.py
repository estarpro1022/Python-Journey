class Schoolmember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized Schoolmember: {}'.format(self.name))

    # def detail(self):a

class Teacher(Schoolmember):
    def __init__(self, name, age, salary):
        # inherit class Schoolmember, 显式调用
        Schoolmember.__init__(self, name, age)
        self.salary = salary
        print('Initialized Teacher: {}'.format(self.name))

    def detail(self):
        print('Name: {}, Age: {}, Salary: {}'.format(self.name, self.age, self.salary))

class Student(Schoolmember):
    # 如果你不调用__init__，会自动继承基本类
    # def __init__(self, name, age, mark):
    #     Schoolmember.__init__(self, name, age)
    #     self.mark = mark
    #     print('Initialized student: {}'.format(self.name))

    def detail(self):
        print('Name: {}, Age: {}, Mark: {}'.format(self.name, self.age, self.mark))

'''input
'''
teacher = Teacher('Mrs.Alake', age = 27, salary = 1000)
student = Student('Kartone', 18)

print()
print(Schoolmember.__doc__)

# '''put it into a list'''
# members = [teacher, student]
# for member in members:
#     member.detail()

