def print_armstrong(n):
    sum=0
    while(n>0):
        r=n%10
        sum=sum+(r**3)
        n=n//10
    return sum

def check(n1,n2):
    for i in range(n1,n2):
        if i==print_armstrong(i):
            print(i)
        else:
            pass

n1,n2=map(int,input("Enter the starting and ending numbers:\n").split(" "))
check(n1,n2)
