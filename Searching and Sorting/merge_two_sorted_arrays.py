# Given two sorted arrays of Size M and N respectively 
# Merge them into a third array such that the third array is also sorted.

n = int(input())
lis =list(map(int,input().split()))
m = int(input())
lis_2 = list(map(int,input().split()))
to_sort = lis + lis_2
to_sort.sort()
print(* to_sort)

# 4
# 4 3 2 1 
# 4
# 8 7 6 5
# 1 2 3 4 5 6 7 8
