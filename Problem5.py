n = 2520

def isDivisibleByOneThroughTwenty(n):
    for i in xrange(1,21):
        if n%i !=0:
            return False
    return True

while (isDivisibleByOneThroughTwenty(n))==False:
    n=n+20
print n

