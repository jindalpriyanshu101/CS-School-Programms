num1 = int(input("Enter your markes of Physics: "))
num2 = int(input("Enter your markes of Chemistry: "))
num3 = int(input("Enter your markes of Mathematics: "))
num4 = int(input("Enter your markes of English: "))
num5 = int(input("Enter your markes of Computer Science: "))

num6 = (num1+num2+num3+num4+num5)/5 
num7 = num1+num2+num3+num4+num5
if num6>=60:
    print("You got 1st division")
elif (num6>=45)&(num6<60):
    print("You got 2nd division")
elif (num6>=33)&(num6<45):
    print("You got 3rd division")
else:
    print("you failed, better luck next time")

print("Your total marks: ", num7)
print(f"You secured {num6} percentage")
