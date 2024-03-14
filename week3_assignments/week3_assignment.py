#creating a function that calculate discount
def calculate_discount(price, discount):

  #if discount is 20% or higher, apply the discount; otherwise, return the original price
  
  if discount > 20:
    return price * (1 - discount/100)
  else:
    return price

customer_one = calculate_discount(100, 21)
print(customer_one)