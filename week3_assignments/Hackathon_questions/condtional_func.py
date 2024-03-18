#Python Conditional Statements
#Prompts a user to enter their age
def user_age():
    age = int(input("Enter your age: \n"))
    #Uses a conditional statement to check if the age is greater than or equal to 18.
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote"
    
print(user_age())