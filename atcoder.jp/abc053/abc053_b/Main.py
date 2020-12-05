S = input()
aIndex = S.index('A')
zIndexs = [i for i, s in enumerate(S) if s == 'Z']
zIndex = zIndexs[-1] + 1
print(len(S[aIndex:zIndex]))