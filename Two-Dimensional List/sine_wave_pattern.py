# Given a two dimensional N*M array, print the array in a sine wave order. 
# i.e. print the first column top to bottom, next column bottom to top and so on.
# Input format :
# N, M, array elements (separated by space)
# Output format :
# Elements of matrix in wave form in a single line and space separated

def sine_wave_print(lis):
    row = len(lis)
    column = len(lis[0])
    for j in range(column):
        if j % 2 == 0:
            for i in range(row):
                print(lis[i][j], end = " ")
        else:
            for i in range(row -1, -1, -1):
                print(lis[i][j], end = " ")    
            
    pass

l = [int(i) for i in input().split()]
m, n = l[0], l[1]
lis = [[l[(j * n) + i + 2] for i in range(n)] for j in range(m)]
sine_wave_print(lis)

# 2 3 1 2 3 4 5 6                       # N.B 2 3 is the size of the array
# 1 4 5 2 3 6