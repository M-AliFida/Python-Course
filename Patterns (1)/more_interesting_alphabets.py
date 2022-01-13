# N = 4
# ABCD
# BCDE
# CDEF
# DEFG

n = int(input())
i = 1
while i <= n:
    j = 1
    first_char = chr(ord('A') + i - 1)
    while j <= n:
        print(chr(ord(first_char)+ j-1), end = '')
        j = j+1
    print()
    i = i + 1