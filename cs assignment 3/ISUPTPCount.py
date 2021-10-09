def ISUPTOCOUNT():
    c=0
    myfile=open('testing.txt','r')
    line = myfile.readline()
    word=line.split()
    for i in word:
        if i == 'IS' or i == 'UP' or i == 'TO':
            c=c+1
    print('IS UP TO Count = ',c)
    myfile.close
ISUPTOCOUNT()