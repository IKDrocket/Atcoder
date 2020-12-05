a = int(input())
s = input()
if a == 0:
    print("Yes")
    exit()
for i in s:
    if i == "+":
        a += 1
    else:
        a -= 1
    if a == 0:
        print("Yes")
        exit()
print("No")