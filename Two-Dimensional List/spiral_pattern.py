# Given an N*M 2D array, print it in spiral form. 
# That is, first you need to print the 1st row, then last column, then last row and then first column and so on.
# Print every element only once.
# Input format :
# Line 1 : N and M, No. of rows & No. of columns (separated by space) followed by N*M  elements in row wise fashion.
# Output format :
# Elements of matrix in spiral form in a single line and space separated

def transform(lis):
    global m, n
    res = [[lis[j][i] for j in range(m)]for i in range(n)]
    m, n = n, m
    res = res[::-1]
    return res

def spiral_print(lis):
    global m, n
    res=[]
    while lis:
        res.append(lis[0])
        del lis[0]
        m -= 1 
        lis= transform(lis)
    for x in res:
        for s in x:
            print(s, end = ' ')

l= [int(i) for i in input().strip().split(' ')]
m, n = l[0], l[1]
lis = [[l[(j * n) + i + 2] for i in range(n)] for j in range(m)]
spiral_print(lis)

# 3 3 1 2 3 4 5 6 7 8 9
# 1 2 3 6 9 8 7 4 5