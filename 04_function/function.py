def maximum(x, y):
    '''Print the maximum number

    Must be integers.'''
    if x > y:
        print(x)
    elif x == y:
        print("The two digits are equal.")
    else:
        print(y)

maximum(1, 2)
print(maximum.__doc__)
help(maximum)
