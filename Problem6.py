def sumOfSquares():
    sum = 0
    for i in xrange(101):
        sum = sum + i**2
    return sum
    
def squareOfSum():
    sum = 0
    for i in xrange(101):
        sum = sum + i
    return sum**2
    
print squareOfSum()-sumOfSquares()