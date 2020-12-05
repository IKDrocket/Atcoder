n = int(input())
a = [0]
a.extend(list(map(int,input().split())))
nums = [0]*(n+1)
for i in a:
    nums[i] += 1

ans = '\n'.join(map(str,nums[1:]))
print(ans)