# Given a 2D integer array of size M*N, 
# Find and print the sum of ith row elements separated by space.

def row_sum(lis):
    arr = []
    for row in lis:
        sum = 0
        for x in row:
            sum = sum + x
        arr.append(sum)
    return arr

m, n =(int(i) for i in input().strip().split(' '))
l = [int(i) for i in input().strip().split(' ')]
lis = [[l[(j * n) + i] for i in range(n)] for j in range(m)]
l = row_sum(lis)
print(*l)

# 4 2 -- this makes array size 8
# 2 2 5 5 7 1 3 4 
# 4 10 8 7 -- (2 + 2) (5 + 5) (7 + 1) (3 + 4)