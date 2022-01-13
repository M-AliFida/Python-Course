# This is a cleaner version of the same exercise done in Patterns (2)
# N = 4
# 1111
# 000
# 11
# 0

n = int(input())
for i in range(0, n):
    for j in range(n - i, 0, -1):
        if(i % 2 == 0):
            print(1, end = "")
        else:
            print(0, end = "")
    print()
