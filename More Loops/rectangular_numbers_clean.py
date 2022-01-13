# This is a cleaner version of the same exercise done in Patterns (2)
# N = 4
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444

n = int(input())
for i in range(1 , n + 1):
    temp = n
    for j in range(1 , i):
        print(temp , end = "")
        temp = temp -1
    for j in range(1, (2 * n) - (2 * i) + 2):
        print(n - i + 1, end = "")
    for j in range(1 , i):
        temp = temp + 1
        print(temp, end = "")
    print()
for i in range(n - 1, 0 , -1):
    temp = n
    for j in range(1, i):
        print(temp, end = "")
        temp = temp - 1 
    for j in range(1, (2 * n) - (2 * i) + 2):
        print(n - i + 1, end = "")
    for j in range(1, i):
        temp = temp + 1
        print(temp, end = "")
    print()