def findBiggestFactor(n):
    d = 2
    while n%d != 0:
        d=d+1
    if d!=n:
        return n/d
    else:
        return d
            
n = 600851475143
d = findBiggestFactor(n)


while n/d != 1:
    n=d
    d=findBiggestFactor(n)
print "The answer is: " + str(d)
    