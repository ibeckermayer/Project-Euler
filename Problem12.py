def generateSequenceOfTriangleNumbers():
    seq = []
    n = 0
    for i in xrange(1,20000):
        n = n+i
        #print "i = " + str(i)
        #print "n = " + str(n)
        seq.append(n)
    return seq
    
def getNumberOfDivisors(n):
    ans = 0
    for i in xrange(1,n+1):
        if n%i==0:
            ans = ans+1
    return ans
        
triangles = generateSequenceOfTriangleNumbers()
removetriangles = list(triangles)

for i in removetriangles:
    print i
    if i%1000 != 0:
        print "^ removed"
        triangles.remove(i)
    else:
        print "NOT REMOVED ##############################################################^^^^^"
    
print getNumberOfDivisors(76576500)
"""
for num in triangles:
    divisors = getNumberOfDivisors(num)
    print str(num) + " has " + str(divisors) + " divisors " 
    if divisors>500:
        print "The value of the first triangle number to have over five hundred divisors is: " + str(num)
        break
"""
