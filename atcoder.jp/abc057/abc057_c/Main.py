def f(a,b):
    return max(len(a),len(b))


ans = 10
n = int(input())
for a in range(1,int(n**0.5)+1):
    if n%a == 0:
        b = int(n/a)
        len_ = f(str(a),str(b))
        ans = min(len_ , ans)
print(ans)