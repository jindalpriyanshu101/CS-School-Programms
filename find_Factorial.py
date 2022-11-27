# easy to find any factorial hehe...

num = int(input("Enter a number: "))  
factorial = 1  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   for i in range(1,num + 1):  
       factorial = factorial*i  # updated value
   print("The factorial of",num,"is",factorial)  

   #1*1 = 1, 1*2 = 2, 2*3 = 6, 6*4=24, this is how factorial will work. hue hue hue