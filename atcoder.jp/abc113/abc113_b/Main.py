n = int(input())
t,a = map(int,input().split())
H = [abs(a-(t-int(x)*0.006)) for x in input().split()]
print(H.index(min(H))+1)