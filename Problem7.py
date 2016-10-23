import math as m 

primes = []
s = 2

def isPrime(s):
    if s == 1:
        return False
    for i in xrange(2,int(m.sqrt(s))+1):
        if s%i==0:
            return False
    return True

while len(primes)<10001:
    if isPrime(s):
        primes.append(s)
    s=s+1
      
print primes[10000]