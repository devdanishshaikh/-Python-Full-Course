list_01 = []
list_01.append(int(input("Enter  your 1st number :")))
list_01.append(int(input("Enter  your 2nd number :")))
list_01.append(int(input("Enter  your 3rd number :")))
list_01.append(int(input("Enter  your 4th number :")))
list_01.append(int(input("Enter  your 5th number :")))

list_02 = list_01.copy()
list_02.reverse()

if list_01 == list_02:
    print("Given list is palindrome")
    print("Original List :", list_01)
    print("after reverse List :",list_02)
else:
    print("Given list is not palindrom1")
    print("Original List :", list_01)
    print("after reverse List :",list_02)
