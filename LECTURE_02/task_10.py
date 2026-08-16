print("==============================================")
name = input("Enter your name: ")
percentage = float(input("Enter your percentage: "))
attendance = int(input("Enter your attendance: "))
family_income = float(input("Enter your family income: "))
sports_achievement = input("Enter your sports achievement (yes/no): ")
disciplinary_record = input("Enter your disciplinary record (good/bad): ")
print("==============================================")
if percentage >= 90 and attendance >= 90 and disciplinary_record.lower() == "good":
    print(name, "is eligible for the Full scholarship.")
elif percentage >= 85 and sports_achievement.lower() == "yes" and disciplinary_record.lower() == "good":
    print(name, "is eligible for the Full Scholarship.")
elif percentage >= 80 and attendance >= 85:
    print(name, "is eligible for the half scholarship.")
elif family_income < 50000 and attendance >= 80 and percentage >= 75:
    print(name, "is eligible for the financial scholarship.")
else :
    print(name, "is not eligible for any scholarship.")