def func(n):
    if n%2==0:
        return False
    else:
        return True

def remove_odd_characters(my_string):
    new_str=my_string
    for i in my_string:
        n=my_string.count(i)
        if func(n) is True:
            new_str=new_str.replace(i,"")
        else:
            pass
    return new_str

my_string=input()
print(remove_odd_characters(my_string))
