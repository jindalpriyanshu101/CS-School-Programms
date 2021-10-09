myfile = open('testing.txt','a')
flist = []
for i in range(3):
    str = input('enter stringgg: ')
    flist.append(str+'\n')
myfile.writelines(flist)
myfile.close
print('Updated the file!!!!!!!!')