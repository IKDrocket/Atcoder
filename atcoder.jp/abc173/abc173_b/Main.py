n = int(input())
s = [input() for _ in range(n)]

nl = ['AC','WA','TLE','RE']
ans = [s.count(n) for n in nl]

for i, a in enumerate(ans):
    print('{} x {}'.format(nl[i],a))