s = input()
c = 0
for i in range(len(s)):
    if s[i].isupper() == True:
        c += 1
if s[0] != "A":
    print("WA")
    exit()
if s[2:-1].count("C") != 1:
    print("WA")
    exit()
if  c != 2:
    print("WA")
    exit()
print("AC")
