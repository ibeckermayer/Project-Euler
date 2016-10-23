def solve():
    i = 1
    ans = 0
    while i<1000:
        if i%3 == 0 or i%5 == 0:
            ans = ans+i
        i = i+1
    print ans
    
solve()
    