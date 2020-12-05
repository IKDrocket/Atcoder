from decimal import *
a, b = input().split()
a = Decimal(a)
b = Decimal(b)

ans = int(a*b)
print(ans)