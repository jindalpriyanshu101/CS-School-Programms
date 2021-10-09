'''
Name: Priyanshu_Aggarwal
Class: XII-D
Assignment: 2
Date of submission: 20-08-2021

'''

print('Ques: Write a python code to pass the nested list to function and add all those values which are at diagonal position and print them')
print('-------------------------------------------------------------')
print('\nInitiating code for given ques... \n')
print("Code Initiated:-\n")


def AddDiagonal(list):
    matrix=0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if i==j:
                matrix +=list[i][j]  # ERROR: Don't do in this way, it wont add diagols, but count them.
            else:
                print('')
    return matrix

a = [[1,2,3],[4,5,6],[7,8,9]]
b = AddDiagonal(a)
print(b)

