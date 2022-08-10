x = int(input("Number daal: "))

if x == 2 or x == 3 or x == 5 or x == 7:
    print("PRIME NUMBER")
elif x%2 == 0 or x%3 ==0 or x%5 == 0 or x%7 == 0:
    print("not a prime number")
else:
    print("its a prime number")