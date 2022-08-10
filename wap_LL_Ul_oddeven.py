L = int(input("Enter lower limit: "))
U = int(input("Enter upper limit: "))

even = 0
odd = 0

for i in range(L,U+1):
   if (i % 2) == 0:
      even += i
   else:
      odd += i

print(f"sum of all even numbers: {even}")

print(f"sum of all odd numbers: {odd}")
