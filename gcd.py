def gcd(a,b):
    if a==0:
        return b
    if a>b:
        a,b=b,a
    return gcd(b-a,a)
print(gcd(168,64))