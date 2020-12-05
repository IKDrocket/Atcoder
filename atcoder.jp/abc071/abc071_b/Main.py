alphabet = "abcdefghijklmnnopqrstuvwxyz"
def solve():
    s = input()
    for i in alphabet:
        if i not in s:
            print(i)
            break
    else:
        print("None")
solve()