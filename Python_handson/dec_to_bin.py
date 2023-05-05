def dec_bin(n):
    return "{0:b}".format(n)
n=eval(input("Enter the decimal number:"))
if n<=0:
    print("Invalid Input")
else:
    print(dec_bin(n))
