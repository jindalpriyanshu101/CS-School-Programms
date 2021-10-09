import os

myfile=open('testing.txt','w')
myfile.write('aur vai ki haal chal')
myfile.close
cwd = os.getcwd
print('success')
print('Container:', cwd)