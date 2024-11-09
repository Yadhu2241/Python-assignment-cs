n = input("Enter the string: ")
n = ''.join(c.lower() for c in n if c.isalnum())
if n == n[::-1]:
    print("True")
else:
    print("False")