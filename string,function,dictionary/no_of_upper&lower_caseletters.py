def find(str):
    words=str.split(" ")
    words="".join(words)
    upp=0
    low=0
    for i in words:
        if i.isupper():
            upp+=1
        elif i.islower():
            low+=1
    print("No of upper case letters are :",upp)
    print("No of lower case letters are :",low)


str=input("Enter a sentence :")
find(str)