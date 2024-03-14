#creating a function with inputs
def large_power(base, exponent):
  base = int(input("Enter your first number as a base. \n"))
  exponent = float(input("Enter your second number as an exponent to the base number. \n"))
  
  #creating a variable to store the result
  result = base ** exponent
  #creating a if statement to check if the result is greater than 5000
  if result > 5000:
    #returning the result
    return True
  else:
    #returning the result
    return False

check_number = large_power(0, 0)
print(check_number)