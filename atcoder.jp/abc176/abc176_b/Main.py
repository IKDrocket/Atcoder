n = list(input())
n = map(int, n)
ans = 'Yes' if sum(n) %9 == 0 else 'No'
print(ans)
