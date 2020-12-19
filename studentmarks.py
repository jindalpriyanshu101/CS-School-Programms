#Name: Priyanshu Aggarwal
#Class: XI - D
#Roll no: 01
#This is code for taking inputs of student's marks then giving them a final score
num1=int(input("Enter your marks of Maths: "))
num2=int(input("Enter your marks of Physics: "))
num3=int(input("Enter your marks of Chemistry: "))
num4= num1 + num2 + num3
num5= 270

if num4 >= num5:
    print("Congo you got", num4, "marks out of 300")

print("Your final score:", num4)