def gcd(a,b):
    if b==0:
        return a
    if a>b:
        return gcd(b,a%b)
    else:
        return gcd(a,b%a)
