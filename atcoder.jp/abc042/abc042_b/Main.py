n,l = input().split()
n = int(n)
s = []
for i in range(n):
    s.append(input())
s.sort()
print("".join(s))