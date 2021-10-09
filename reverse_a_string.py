def reverse(str):
    s = "" #leaved empty
    for ch in str:
        s = ch + s
    return s


# given string
s1 = str(input("enter string: "))
print("Given String: ", s1)

# reversed string
print("Reversed String: ", reverse(s1))