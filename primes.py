import math
import datetime
def getprimes(P):
    primes = [0]*(P+1)
    for i in range(2,int(math.sqrt(P))+1):
        if primes[i]==0:
            j = i*2
            while j <=P:
                primes[j]=1
                j += i
    count = 0
    value=[]
    for i in range(2,P+1):
        if primes[i]==0:
            value.append(i)
            count +=1
    return value


print getprimes(10)