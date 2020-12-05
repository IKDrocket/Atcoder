def c_kth_substring(S, K):
    tmp = []
    for i in range(len(S)):
        for j in range(i + 1, i + K + 1):
            if j <= len(S):
                tmp.append(S[i:j])
    tmp = sorted(set(tmp))
    ans = tmp[K - 1]
    return ans
 
S = input().strip()
K = int(input())
print(c_kth_substring(S, K))