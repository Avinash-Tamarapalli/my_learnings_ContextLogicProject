from sys import exit

n=int(input("Enter the no. of movies:"))
if n<=0:
    print("Invalid Number")
    exit()
else:
    pass
mn,my,m=[],[],[]
print("Enter the movie names:")
for i in range(n):
    mn.append(input())
for i in range(n):
    print("Enter the release year of movie",i+1,":")
    y=int(input())
    if y<2000 or y>2017:
        print("Invalid release year")
        exit()
    else:
        my.append(y)

for i in range(n):
    m.append(my[i])
    m.append(mn[i])
print("The new list is:")
print(m)
