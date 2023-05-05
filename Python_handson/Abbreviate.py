def abbreviate(college_name):
    s=""
    for i in college_name:
        if i.isupper():
            s+=i
        else:
            pass
    return s

college_name=input()
print(abbreviate(college_name))
