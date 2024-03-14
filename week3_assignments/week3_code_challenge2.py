#creating a function divisible by ten
def divisble_by_ten(num):
    num = int(input("Enter your number without decimal points. \n"))
    if num % 10 == 0:
        return True
    else:
        return False
num_to_check = divisble_by_ten(0)
print(num_to_check)