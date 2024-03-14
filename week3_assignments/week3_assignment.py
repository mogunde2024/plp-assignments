#creating a function that calculate discount
def calculate_discount(price, discount):
  price = float(input("Enter the price of the item. \n"))
  discount = float(input("Enter percentage discount the item qualifies. \n"))

  #if discount is 20% or higher, apply the discount; otherwise, return the original price
  
  if discount > 20:
    return price * (1 - discount/100)
  else:
    return price

customer_one = calculate_discount(0 , 0 )
print("The selling price of the item is USD {}.".format(customer_one))