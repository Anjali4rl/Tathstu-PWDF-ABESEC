mydic={'B':'Ball','J':'Joker','R':'Raymond','D':'Django','A':'Avacado'}


def sortbykey(mydic):
    for key in sorted(mydic.keys()):
        print(key, ':', mydic[key])
def sum_length(mydic):
    sum=0
    for key in sorted(mydic.keys()):
        x=mydic[key]
        p=len(x)
        sum+=p
    return (sum)
def reversedvalues(mydic):
    print("Reversed values are :",end="")
    for key in mydic.keys():
        print(mydic[key][::-1],end=" ")

print(mydic)
print()
sortbykey(mydic)
print("The sum of length of all values are : ",sum_length(mydic))
print(mydic)
print()
print(reversedvalues(mydic))
