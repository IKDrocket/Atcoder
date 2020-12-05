a,b = input().split()
num = int(a+b)
for i in range(1,10101):
    ans = i*i
    if num == ans:
        print("Yes")
        break
else:
    print("No")
