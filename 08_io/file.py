poem = '''\
hello world.
I'm fine'''

'''test'''
file = open('test.txt', 'w')
# 覆盖，需要谨慎
file.write('hello')
file.close()

file = open('hello.txt')

while True:
    # line 中自带状况
    line = file.readline()
    if len(line) == 0:
        break;

    print(line, end = '')

