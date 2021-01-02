a, b = input().split()
ans = max(sum(map(int, list(a))), sum(map(int, list(b))))
print(ans)