a,b,c = input().split()
print(max(int(a+b)+int(c),int(b+c)+int(a),int(c+a)+int(b)))