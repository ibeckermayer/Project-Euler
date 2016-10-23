n=999

def palindromes(n):
    palindromes = []
    while n>=100:
        p = n
        while p>=100:
            potentialP = n*p
            if isPalindrome(potentialP):
                palindromes.append(potentialP)
            p=p-1
        n=n-1
    return palindromes
        
def isPalindrome(n):
    s = str(n)
    if s==s[::-1]:
        return True
    else:
        return False
        
def findGreatest(l):
    d=0
    for i in l:
        if i>d:
            d=i
    return d
    
print findGreatest(palindromes(n))
        