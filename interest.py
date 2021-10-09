def interest(principle,rate,time):
    print("Interest from given values: ", (principle*rate*time)/100)

n1= float(input("Enter principle value: "))
n2= float(input("Enter rate amount: "))
n3= float(input("Enter time taken: "))
interest(n1,n2,n3)