def count_chars(str):
     upper, lower, num, special = 0, 0, 0, 0
     for i in range(len(str)):
          if str[i] >= 'A' and str[i] <= 'Z': upper += 1
          elif str[i] >= 'a' and str[i] <= 'z': lower += 1
          elif str[i] >= '0' and str[i] <= '9': num += 1
          else: special += 1
     return upper, lower, num, special
           
str = str(input("enter string: "))
print("Original Substrings:",str)
u, l, n, s = count_chars(str)
print('\nUpper case characters: ',u)
print('Lower case characters: ',l)
print('Number case: ',n)
print('Special case characters: ',s)
