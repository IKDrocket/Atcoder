num = list(input())
n = int(num[-1])
if n == 3:
    print('bon')
elif n in [2,4,5,7,9]:
    print('hon')
else:
    print('pon')