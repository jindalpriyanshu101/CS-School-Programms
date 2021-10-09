num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

large = num1
if large<num2:
    large = num2
if large<num3:
    large = num3

print("Largest number you provided:", large)