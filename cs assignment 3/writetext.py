myfile = open('testing.txt','w')
for i in range(3): # 3=number of lines to write.
    str = input('Enter queries to write: ')
    myfile.write(str)
    myfile.write('\n')
myfile.close
#file= myfile.readlines()
print("saved successfully!!!!")