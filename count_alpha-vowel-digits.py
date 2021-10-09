'''
Name: Priyanshu_Aggarwal
Class: XII-D
Assignment: 2
Date of submission: 26-08-2021 

'''

print('Ques1: Write a python code to pass a string into the function and count the numbers of alphabets, vowels and number of digits?')
print('-------------------------------------------------------------')
print('\nInitiating code for given ques...\n')
print("Code Initiated:-\n")


def count(str):

	# Declaring the variable vowels, number, alphabets.
	vowels = 0
	consonants = 0
	digit = 0

	# now using str.length() function to count vowel etc in given string.

	for i in range(0, len(str)):
		
		ch = str[i]

		if ( (ch >= 'a' and ch <= 'z') or
			(ch >= 'A' and ch <= 'Z') ):

			# To handle upper case letters
			ch = ch.lower()

			if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
				vowels += 1
                

            # NOTE: (ch == ('a','e','i','o','u')) will not work here, idk why...    

			else:
				consonants += 1
		
		elif (ch >= '0' and ch <= '9'):
			digit += 1
		
	
	print("Vowels:", vowels)
	print("Consonant:", consonants)
	print("Digit:", digit, '\n ----------------------End of code----------------------')
    


# Lines to run the function now.
str = input("Enter string: ")
count(str)
