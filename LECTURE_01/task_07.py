product = input("Enter product name : ")
price = float(input("Enter product price : "))
Quantity =int(input("Enter product quantity : "))
discount = float(input("Enter discount percentage : "))
customer_paid = int(input("Enter amount paid by customer : "))
total_price = price * Quantity
discount_amount = (discount / 100) * total_price
final_price = total_price - discount_amount
change = customer_paid - final_price

print("*********Product Price Calculator*********")
print(f"\tProduct: {product}")
print(f"\tPrice: {price}")
print(f"\tQuantity: {Quantity}")
print(f"\tTotal Price: {total_price}")
print(f"\tDiscount Amount: {discount_amount} ")
print(f"\tFinal Price: {final_price}")
print(f"\tCustomer Paid: {customer_paid}")
print(f"\tChange: {change}")
print("*********Thank you For Shopping*********")