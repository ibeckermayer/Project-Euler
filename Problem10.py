from Problem7 import isPrime


def generatePrimeSequenceBelow2Million():
    ps = []
    for i in xrange(2000000):
        if isPrime(i):
            ps.append(i)
    return ps
    
    
ps = generatePrimeSequenceBelow2Million()

sum = 0
for number in ps:
    sum = sum+number
    #print "number = " + str(number)
    #print "sum = " + str(sum)
    
print "sum = " + str(sum)