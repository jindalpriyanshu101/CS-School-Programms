myfile = open("testing.txt", "r")
str = myfile.read()

vowels =  0
for i in str:
    if( i=='A' or i=='a' or i=='E' or i=='e' or i=='I'
        or i=='i' or i=='O' or i=='o'
	    or i=='U' or i=='u'):
        	vowels +=1
        

print('The Number of Vowels in text file :', vowels)