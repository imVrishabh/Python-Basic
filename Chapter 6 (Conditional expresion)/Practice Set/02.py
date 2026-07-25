# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass.
# Assume 3 subjects and take marks as an input from the user. 

a= int(input("Python Marks:"))
b= int(input("DSA Marks:"))
c= int(input("OS Marks:"))

if (a<33) or (b<33) or (c<33):
    print("You have failed because you have less than 33% in one or more subjects.")
elif (a+b+c)/3 <40:
    print("You have failed because your overall percentage is less than 40%.")
else:
    print("Congratulations! You have passed the exam.")
    