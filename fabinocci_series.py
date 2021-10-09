# Program to display the Fibonacci sequence up to n-th term

num = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if num <= 0:
   print("Please enter a positive integer")  # it will cause error because (-1)+(0) = -1; and it will not increase for further values
elif num == 1:
   print("Fibonacci sequence upto",num,":") # to show that program started to write fibonacci
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < num:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1   # it means adding of +1 in 'count'