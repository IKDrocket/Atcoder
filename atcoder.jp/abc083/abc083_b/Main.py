n, a, b = map(int, input().split())
sum_all = 0
for i in range(1,n+1):
    sum = 0
    i_ = i
    while i_ > 0:
        sum += i_ % 10
        i_ //= 10
    if a <= sum <= b:
        sum_all += i
print(sum_all)