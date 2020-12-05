money = 100
x = int(input())
count = 0
while money < x:
    money = int(money * 1.01)
    count += 1
print(count)