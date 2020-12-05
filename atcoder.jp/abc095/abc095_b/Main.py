n, x = map(int,input().split())
array = [int(input()) for i in range(n)]

cnt = 0

x -= sum(array)
cnt += len(array)
cnt += x // min(array)

print(cnt)