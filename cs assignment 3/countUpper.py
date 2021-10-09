myfile = open('testing.txt','r')
str = myfile.read()
def Count(str):
    upper, number = 0, 0
    for i in range(0, len(str)):
        if str[i].isupper():
            upper += 1
        elif str[i].isdigit():
            number += 1
    print('Upper case letters:', upper)
    print('Number:', number)
myfile.close
Count(str)