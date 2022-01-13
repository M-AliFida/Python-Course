# You are given an integer array A that contains only integers 0 and 1. 
# Write a function to sort this array. 
# Find a solution which scans the array only once. Don't use extra array.

n = int(input())
lis = [int (x) for x in input().split() [:n]]
zeros = 0
ones = 0

for i in lis:
    if i == 0:
        zeros = zeros + 1
    else:
        ones = ones + 1
lis = []

for i in range(0, zeros):
    lis.append(0)
for i in range(0, ones):
    lis.append(1)
        
for x in lis:
    print(x, end = ' ')

# 5
# 0 1 0 1 0
# 0 0 0 1 1