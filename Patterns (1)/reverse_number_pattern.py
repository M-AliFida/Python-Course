# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 21
# 321
# 4321

last_n = int(input())
for row in range(1, last_n + 1):
    for column in range(row, 0, -1):
        print(column, end='')
    print("")