'''
Name: Priyanshu_Aggarwal
Class: XII-D
Assignment: 2
Date of submission: 26-08-2021 

'''

print('Ques: Passing dictionary to function with list and stores the value of list as key and its frequency or no. of occurrence as value')
print('-------------------------------------------------------------')
print('\nInitiating code for given ques... \n')
print("Code Initiated:-\n")

def frequencyCount(list,unknown):
    for i in list:
        if i not in unknown:
            unknown[i]=1

        else:
            unknown[i]+=1

    return unknown
    

list = input("Enter numbers with <space> b/w them: ")
a = list.split()
b = {}
frequencyCount(a,b)
print(b)
print("-----------------------END OF CODE----------------")