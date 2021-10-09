x = str(input("enter string: "))
 
w = ""
for i in x:
    w = i + w
 
if (x == w):
    print("Yes its palindrome")
else:
    print("No its not")
