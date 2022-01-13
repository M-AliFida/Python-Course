# Returns largest column sum with corresponding index value.

def column_sum(lis):
    n = len(lis)
    m = len(lis[0])
    max_s = -1
    max_i = -1
    for j in range(m):
        sum = 0
        for ele in lis:
            sum += ele[j]
        if sum > max_s:
            max_s = sum
            max_i = j
    return max_s, max_i

lis = [[5, 1, 2, 3], [5, 4, 5, 6], [5, 7, 8, 9]]
max_sum, max_index = column_sum(lis)
print(max_sum, max_index)

# 18 3