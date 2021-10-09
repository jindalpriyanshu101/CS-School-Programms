'''
Name: Priyanshu_Aggarwal
Class: XII-D
Assignment: 2
Date of submission: 26-08-2021 

'''

print('Ques: Write a python code to input n numbers in tuple and pass it function to add the even and odd numbers separately and output them?')
print('-------------------------------------------------------------')
print('\nInitiating code for given question... \n')
print("Code Initiated:-\n")
def CountOddEven(tuple):
    even= 0
    odd= 0
    
    for i in tuple:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

tuple=()
n = int(input("Enter number of tuples: "))
for i in range(n):
    num = int(input("Enter numeberrr: "))
    tuple = tuple + (num,)

oecount = CountOddEven(tuple)
print('No. of Odds: ', oecount[1], "No. of evens: ", oecount[0])
print("\n ----------------End of code---------------\n")