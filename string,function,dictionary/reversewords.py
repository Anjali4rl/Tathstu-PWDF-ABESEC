def rev(st):
    words=st.split(" ")
    words=words[-1::-1]
    revst=" ".join(words)
    print(revst)

st=input()
rev(st)
