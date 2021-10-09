sale = int(input("Enter sales of this month:" ))
if sale>500000:
    comission = sale * (10/100)
else:
    comission = sale * (5/100)

print("Your comission is:", comission)