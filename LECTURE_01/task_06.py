std_name = input("Enter your name : ")
sub_1 = int(input("Enter marks of subject 1 : "))
sub_2 = int(input("Enter marks of subject 2 : "))
sub_3 = int(input("Enter marks of subject 3 : "))
sub_4 = int(input("Enter marks of subject 4 : "))
sub_5 = int(input("Enter marks of subject 5 : "))

total_marks = 500
obtained = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
average_marks = obtained / 5
percentage = (obtained / total_marks) * 100

print("*****Student Marks Calculator*****")
print(f"Name: {std_name}")
print(f"Total Marks: {total_marks}")
print(f"Obtained Marks: {obtained}")
print(f"Average Marks: {average_marks}")
print(f"Percentage: {percentage}%")