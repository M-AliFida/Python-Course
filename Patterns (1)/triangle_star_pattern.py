# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# *
# **
# ***
# ****

n = int(input())
for i in range(0, n):
    for j in range(0, i+1):
        print("*", end = "")
    print()