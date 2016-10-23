import math

def findPythagoreanTripletWhoseSumIs1000():
    for a in xrange(500):
        for b in xrange(500):
            c = math.sqrt(a**2+b**2)
            print str(a) + " + " + str(b) + " + " + str(c) + " = " + str(a+b+c)
            if a+b+c == 1000:
                print a*b*c
                return a*b*c

findPythagoreanTripletWhoseSumIs1000()