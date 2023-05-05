#wrong

from sys import exit
def printf(d):
    if d=={}:
        print("Here's the dictionary you've created:")
        print(d)
    else:
        print("Here's the dictionary you've created:")
        for k,v in d.items():
            print(k,v,sep=":")

def main(d):
    m=[]
    word=input("Enter the word:\n")
    num_mean=int(input("Enter the no of meanings:\n"))
    if num_mean<=0:
        print("Invalid Input")
        printf(d)
        exit()
    else:
        pass
    print("Enter the meanings:")
    for i in range(num_mean):
        m.append(input())
    d[word]=m
    turn = int(input("Do you want to add one more elements to the dictionary? If yes, press 1, else press 0:\n"))
    return d,turn
d={}
word_dict =main(d)
if word_dict[1]==1:
    word_dict =main(word_dict[])
print(word_dict[0])
