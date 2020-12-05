s = list(input())
count = 0
for i in s:
    if i == 'x':
        count += 1
if count >= 8:
    print('NO')
else:
    print('YES')