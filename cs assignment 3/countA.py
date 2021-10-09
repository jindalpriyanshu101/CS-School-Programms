def letterFrequency(filename, letter):
    # open file in read mode
    file = open('testing.txt', 'r') #path: E:\\School Assignments\\CS Programms\\cs assignment 3\\testing.txt
  
    # store content of the file in a variable
    text = file.read()
    print(text)
    # using count()
    return text.count(letter)
  
  
# call the function and display the letetr count
print(letterFrequency('testing.txt', 'a'))