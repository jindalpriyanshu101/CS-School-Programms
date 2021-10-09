# Your code to convert using if else @nivas

unit = str(input("Is your temp currently in Fahrenheit(F) or Celsius(C)? Please enter F or C: "))

if unit == "f" or unit == "F":  
  print("Your entered temperature will now be transformed from Fahrenheit to Celsius")
  temp = int(input("Enter your temp in Fahrenheit: "))
  new_tempC = (temp - 32) * 5/9
  print(f"{temp} F expressed in Celsis is {new_tempC} C.")

elif unit == "c" or unit == "C":  
  print("Your entered temperature will now be transformed from Celsius to Fahrenheit")
  temp1 = int(input("Enter your temp in Celsius: "))
  new_tempF = (temp1 * 9/5) - 32
  print(f"{temp1} C expressed in Fahrenheit is {new_tempF} F.")

else:
  print("Please enter a valid input.")