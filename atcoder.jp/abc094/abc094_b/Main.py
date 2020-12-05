n,m,x = map(int,input().split())
a = list(map(int,input().split()))
count = 0
for i in a:
    if i < x:
        count += 1
    else:
        break
print(min(count,m-count))