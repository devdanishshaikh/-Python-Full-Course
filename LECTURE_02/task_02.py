# Email Checker-Task 2
email = input("Enter your Email : ")
if email.endswith("@gmail.com"):
    print("Gmail account")
    print("Email :", email)
elif email.endswith("@yahoo.com"):
    print("Yahoo account")
    print("Email :", email)
elif email.endswith("@outlook.com"):
    print("Outlook account")
    print("Email :", email)
elif email.endswith("@hotmail.com"):
    print("Hotmail account")
    print("Email :", email)
else:
    print("Invalid Email")