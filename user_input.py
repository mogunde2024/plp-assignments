#massage that prompt user input
name = input("What is your name? \n").title()
age = input("How old are you? \n")
location = input("Where do you live? \n").title()

message = "Hello {} you are {} years old and live in {}.".format(name, age, location)

print(message)
