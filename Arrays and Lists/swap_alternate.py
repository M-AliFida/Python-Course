# Given an array of length N, swap every pair of alternate elements in the array.

n = int(input())
lis = [int(x) for x in input().split()]
length = len(lis)
if length % 2 == 1:
    length = length - 1 
for i in range(0, length, 2):
    lis[i], lis[i+1] = lis[i+1], lis[i] 

print(lis)

# 6
# 1 2 3 4 5 6
# [2, 1, 4, 3, 6, 5]