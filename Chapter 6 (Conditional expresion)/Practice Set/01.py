# 1. Write a program to find the greatest of four numbers entered by the user.
a= int(input("enter the first number"))
b= int(input("enter the second number"))
c= int(input("enter the third number"))
d= int(input("enter the fourth number"))
# print("the greatest number is", max(a,b,c,d))
if (a>b) and(b>c) and (c>d): 
    print("Greatest number is a:",a)

elif(b>a) and(b>c) and (b>d):
    print("Greatest number is b:",b)
elif(c>a) and(c>b) and (c>d):
    print("Greatest number is c:",c)
elif(c>a) and (c>b) and (d>c):
    print("Greatest number is d:",d)
elif(d>a) and (d>b) and (d>c):
    print("Greatest number is d:",d)

