class Robot:
    population = 0
    def __init__(self, name):
        self.name = name
        Robot.population += 1   # 类变量，用Robot.population，共享的

    def say_hi(self):
        print('hello')

    # 类变量用Robot.parameter to access
    # 在对象的方法中，对象变量用self.parameter to access

robot1 = Robot('robot1')
print(robot1.name)
robot2 = Robot('robot2')
# 由于类变量共享，population + 1
print(robot1.population)



# def myfunction(v1):
#     if v1 == 0:
#         print("Value: Zero")
#     elif v1 == 1:
#         print("Value: One")
#     elif v1 >= 2:
#         print("Value: Greater then 1")
#
# v1 = 1
#
# myfunction()
#
