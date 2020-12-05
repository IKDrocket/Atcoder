import fractions

a,b,c,d = map(int,input().split())
tn = b-a+1

cn = (b//c)-(a-1)//c
dn = (b//d)-(a-1)//d
cd = (c*d)//fractions.gcd(c, d)
cdn = (b//cd)-(a-1)//cd

print(tn-cn-dn+cdn)