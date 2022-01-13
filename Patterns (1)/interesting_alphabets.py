# Print the following pattern for the given number of rows.
# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE

n= int(input())
for i in range (n, 0, -1):
    for j in range(i, n + 1):
        print(chr(j + 64), end = "")
    print("")