a = int(input("Enter your age: "))

#if statement no.1
if(a%2):
    print("a is even")
#end of if statement no.1 

# if statement no.2
if(a>18):
    print("You are eligible to vote")

elif(a<0):
    print("you are entering wrong age")

elif(a==0):
    print("its not possible to have age")

else:
    print("you are above the age of consent")
# end of  if statement no.2

print("thank you") 