n = int(input()) 
num = [0,0,0,0,0]

for i in range(n):
    s = input()
    if s[0]=='M':
            num[0] += 1
    elif s[0]=='A':
            num[1] += 1
    elif s[0]=='R':
            num[2] += 1
    elif s[0]=='C':
            num[3] += 1
    elif s[0]=='H':
            num[4] += 1

num_1 = num[0]*num[1]*num[2]
num_2 = num[0]*num[1]*num[3]
num_3 = num[0]*num[1]*num[4]
num_4 = num[1]*num[2]*num[3]
num_5 = num[1]*num[2]*num[4]
num_6 = num[2]*num[3]*num[4]
num_7 = num[0]*num[2]*num[3]
num_8 = num[0]*num[2]*num[4]
num_9 = num[0]*num[3]*num[4]
num_10 = num[1]*num[3]*num[4]

answer = num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7 + num_8 + num_9 + num_10
print(answer)