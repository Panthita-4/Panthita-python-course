# Complete this program to classify people by age

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

age =int(input("Enter your age:"))
if age <=12:
    print("your are a Child")
elif 13<=age<=19:
    print("your are a Teenager")
elif 20<=age<=59:
    print("you are an Adult")
else :
    print("you are a Senior")