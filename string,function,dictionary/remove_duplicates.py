def rem(st):
    charset=set()
    withoutdup=""
    for c in st:
        if c not in charset:
            charset.add(c)
            withoutdup+=c
    return withoutdup
st=input("Enter a String :")
print("The string without duplicates is : ",rem(st))

