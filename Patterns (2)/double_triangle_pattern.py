# N = 5
#     1
#    121
#   12321
#  1234321
# 123454321

n = int(input())
i = 1
while i <= n:
    s = 1
    while s <= (n - i):
        print(" ", end = '')
        s = s + 1
    inc_num = 1
    while inc_num <= i:
        print(inc_num, end = '')
        inc_num = inc_num + 1
    sec_num = inc_num - 2
    while sec_num > 0:
        print(sec_num, end = '')
        sec_num = sec_num - 1
    print()
    i = i + 1