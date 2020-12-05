import math

a,b,h,m = map(int,input().split())

ar = (h + m/60)/12 * 360
br = m/60 * 360

cc = (a**2 + b**2) - 2*a*b*math.cos(math.radians(abs(ar-br)))

ans = math.sqrt(cc)


print(ans)