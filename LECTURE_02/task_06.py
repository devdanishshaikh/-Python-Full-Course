# Advanced Student Admission Eligibility
print("==============================================")
print("\t\t College Admission System\t\t")
print("==============================================")

std_name = input("Student Name : ")
std_age =int(input("Student Age : "))
matric_per =float(input("Matric Percentage : "))
intermediate_per =float(input("Intermediate Percentage : "))
entrytest_marks =float(input("Entry Test Marks : "))
interview_score =float(input("Interview Score : "))
domicile = input("Domicile : ")

# default values
admission_status = "Not ELigible"
category = "None"

if std_age >=16 and std_age <=25:

    if matric_per >= 60 and intermediate_per >=60:

        if entrytest_marks >=70:

            if interview_score >=60:

                if domicile =="sindh" or domicile =="Sindh":

                    admission_status = "Eligible"

                    if matric_per >=80 and intermediate_per >=80 and entrytest_marks >=85:

                        category = "Merit"
                    else:

                        category = "Regular"

                elif domicile !="sindh" and domicile !="Sindh":

                    if entrytest_marks >=85:

                        admission_status = "Eligible"

                        category = "Open Merit"

                    else:

                        admission_status = "Not Eligible"

                        category = "None"
                        
                else:

                    admission_status = "Not Eligible"

                    category = "None"

            else:

                print("Not Eligible: interview score requirement not met")

        else:

            print("Not Eligible: Entry test requirement not met")

    else:

        print("Not Eligible: Academic requirement not met")

else:

    print("ot Eligible: Age requirement not met")

print("==============================================")
print("\t \t Admission Result")
print("==============================================")
print("Student Name : ", std_name)
print("Student Age : ", std_age)
print("Matric Percentage : ", matric_per)
print("Intermediate Percentage : ", intermediate_per)
print("Entry Test Marks : ", entrytest_marks)
print("Interview Score : ", interview_score)
print("Domicile : ", domicile) 
print()
print("Admission Status : ", admission_status)
print("Category : ", category)
print("===============================================")