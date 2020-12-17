import math

def combinations_count(n, r):
    try:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    except:
        return 0
        
n,m = map(int,input().split())
print(combinations_count(n,2)+combinations_count(m,2))