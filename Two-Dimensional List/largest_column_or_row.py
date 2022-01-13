# Given an NxM 2D array, you need to find out which row or column has largest sum (sum of its elements) overall 
# Amongst all rows and columns.
# If equal, column will be printed. 

def largest_row_col(lis):
    list = []
    n = len(lis)
    m = len(lis[0])
    max_row = -1
    row_index = -1
    max_column = -1
    column_index = -1
    for i in range(n):
        sum = 0
        for j in range(m):
            sum = sum + lis[i][j]
        if sum > max_row:
          max_row = sum
          row_index = i             
    
    for j in range(m):
        sum_1 = 0 
        for i in range(n):
            sum_1 = sum_1 + lis[i][j]
        if sum_1 > max_column:
          max_column = sum_1
          column_index = j
    
    if max_row == max_column and row_index < column_index or max_row > max_column:
        list.append("row")
        list.append(max_row)
        list.append(row_index)
            
    else: 
        list.append("column")
        list.append(max_column)
        list.append(column_index)

    return list


m, n = (int(i) for i in input().strip().split(' '))
l = [int(i) for i in input().strip().split(' ')]
lis = [[l[(j * n) + i] for i in range(n)] for j in range(m)]
l = largest_row_col(lis)
print(* l)

# 3 3
# 1 2 3 4 5 6 7 8 9
# row 24 2 

# row/ column - maximum value - index