# N = 5
#     1
#    12
#   123
#  1234
# 12345

n = int(input())
i = 1
while i <= n:
    s = 1
    while s <= n-i:
        print(" ", end = '')
        s = s + 1
    inc_num = 1
    while inc_num <= i:
        print(inc_num, end = '')
        inc_num = inc_num + 1
    print()
    i = i + 1