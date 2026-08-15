def hello(name):
    print("Hello {}".format(name))

hello('Allice')

hello('Vrishabh')


'''///'''
'''function wiht return value'''

import random
def getAnswer(answerNumber):
    if answerNumber ==1 :
        return 'It is certain'
    elif answerNumber ==2 :
        return 'It is decidely go'
    elif answerNumber ==3 :
        return 'Yes'
    elif answerNumber ==4 :
        return 'Reply hazy  try again'
    elif answerNumber ==5 :
        return 'Ask again later'
    elif answerNumber ==6 :
        return 'Concentrate and ask again'
    elif answerNumber ==7 :
        return 'My reply is no'
    elif answerNumber ==8:
        return 'No'
    elif answerNumber ==9 :
        return 'Very doubtfull'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
