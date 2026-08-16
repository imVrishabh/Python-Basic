'''         Example-1           '''

def spam(divideBy):
    try:
        return 42 / divideBy
    excpect ZeroDivisionError as e:
        print('Error: Invalid argument: {}' .format)



print(spam(2))
print(spam(23))
print(spam(0))
print(spam(1))


