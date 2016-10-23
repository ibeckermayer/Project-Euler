def generateFibonacciSequenceLessThan4000000():
    fs = [1,2]
    while (fs[len(fs)-1]+fs[len(fs)-2])<=4000000:
        fs.append(fs[len(fs)-1]+fs[len(fs)-2])
    return fs

fibonacciSequence = generateFibonacciSequenceLessThan4000000()

ans = 0
for num in fibonacciSequence:
    if num%2==0:
        ans = ans+num
print ans
    