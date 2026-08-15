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
print(f"    Product: {product}")
print(f"    Price: {price}")
print(f"    Quantity: {Quantity}")
print(f"    Total Price: {total_price}")
print(f"    Discount Amount: {discount_amount} ")
print(f"    Final Price: {final_price}")
print(f"    Customer Paid: {customer_paid}")
print(f"    Change: {change}")
print("*********Thank you For Shopping*********")