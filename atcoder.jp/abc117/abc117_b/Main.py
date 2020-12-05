n = int(input())
l = [int(i) for i in input().split()]
ans = 'No'
if max(l) < sum(l)-max(l):
    ans = 'Yes'
print(ans)