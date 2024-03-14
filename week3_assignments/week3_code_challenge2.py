#creating a function divisible by ten
def divisble_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False
num_to_check = divisble_by_ten(346)
print(num_to_check)