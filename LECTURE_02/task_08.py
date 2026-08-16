print("===============================")
a = int(input("Enter value of a :"))
b = int(input("Enter value of b :"))
c = int(input("Enter value of c :"))
print("===============================")
print("Value of a :", a)
print("Value of b :", b)
print("Value of c :", c)
print("===============================")

if a > b and a > c:
  print(a, "is the largest number")
elif b > a and b > c:
  print(b, "is the largest number")
else:
  print(c, "is the largest number")