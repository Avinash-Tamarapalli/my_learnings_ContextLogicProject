from sys import exit
def feedback(gl,gf):
    l,i=[],0
    while(i<len(gf) or i<len(gl)):
        if gf[i]==gl[i]:
            l.append("equal")
        else:
            l.append(gl[i]-gf[i])
        i+=1

    return l


gl,gf=[],[]
n=int(input())
if n<=0:
    print("Invalid list size")
    exit()
else:
    pass
for i in range(n):
    a=int(input())
    if a<0:
        print("Invalid input")
        exit()
    else:
        gl.append(a)
for i in range(n):
    a=int(input())
    if a<0:
        print("Invalid input")
        exit()
    else:
        gf.append(a)


print(feedback(gl,gf))
