s = input()
ans = 0
if s == 'RSR':
    ans = 1
else:
    ans = s.count('R')
print(ans)