import random
for i in range(5):
    print(random.randint(1,10))

# import anything using this [ form random import *]

'''////'''
''' If want to end a program early use this '''
import sys

while True:
    print('True exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed {}.'.format(response))

    