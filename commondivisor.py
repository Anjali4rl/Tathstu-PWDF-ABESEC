

def gcd(a,b):
   small=min(a,b)
   for i in range(1,small+1):
        if(a%i==0) and (b%i==0):
            p=i
            print(p)

a,b=map(int,input().split())
gcd(a,b)

