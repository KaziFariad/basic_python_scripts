price = int(input("Enter the price: "))
discount = int(input("Enter percentage of discount: "))
to_pay = (1-(discount/100)) * price
print("Amount to be paid after discount is:", to_pay)
