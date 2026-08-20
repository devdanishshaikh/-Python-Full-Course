product = {"name": "Laptop", "price": 85000, "brand": "Dell"}
print(product["price"])
print(f"{product['brand']} {product['name']} costs {product['price']}")
print(product.get("brand"))