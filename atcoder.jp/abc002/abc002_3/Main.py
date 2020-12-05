a,b,c,d,e,f  = map(int, input().split())

a = a - e
b = b - f
c = c - e
d = d - f

T = abs((a*d-b*c)/2)
print(T)
