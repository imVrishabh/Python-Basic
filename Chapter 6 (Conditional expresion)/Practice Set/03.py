# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 

comment= input("Enter your comment: ")      
spam_keywords= ["Make a lot of money", "buy now", "subscribe this", "click this"]
is_spam= False
for keyword in spam_keywords:
    if keyword in comment:
        is_spam= True
        break   
if is_spam:
    print("This comment is spam.")
else:
    print("This comment is not spam.")