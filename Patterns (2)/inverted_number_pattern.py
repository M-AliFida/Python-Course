# N = 5
# 55555
# 4444
# 333
# 22
# 1

n = int(input())
for i in range(n, 0, -1):
    for j in range(0, i):
        print(i, end = '')
    print("")