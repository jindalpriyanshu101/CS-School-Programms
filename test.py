dic = {}

while True :
      emp = int(input("Emp id: "))
      name = input("Enter emp name: ")
      sl = int(input("Enter emp salary: "))
      dic[emp] = {name:sl}
      check = input('add more?[y/n]:' )
      if check == 'y':
          continue
      else:
          break
for x in dic:
    for y in dic[x]:
        if dic[x][y]>20000:

            print (f"Emp id: {x};", f"name: {y};", f"salary: {dic[x][y]}")


