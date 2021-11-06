def oddeven(num):
   if (num % 2) == 0:
      print(num, "is Even")
   else:
      print(num, "is Odd") 

num = int(input("Enter number: "))
oddeven(num)