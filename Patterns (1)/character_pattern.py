# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# A
# BC
# CDE
# DEFG

n = int(input())
row = 1
while row <= n:
    column =1
    ch = ord('A') + row - 1
    while column <= row:
        print(chr(ch + column - 1), end= "")
        column += 1
    print()
    row += 1