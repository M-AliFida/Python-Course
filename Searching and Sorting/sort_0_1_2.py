# You are given an integer array containing only 0s, 1s and 2s. 
# Write a solution to sort this array using one scan only.

n = int(input())
lis = [int (x) for x in input().split() [:n]]
zeros = 0
ones = 0
twos = 0
for i in lis:
    if i == 0:
        zeros += 1
    elif i == 1:
        ones += 1
    else:
        twos += 1

lis = []
for i in range(0, zeros):
    lis.append(0)
for i in range(0, ones):
    lis.append(1)
for i in range(0, twos):
    lis.append(2)
         
for x in lis:
    print(x, end = ' ')

# 5
# 0 1 0 0 1
# 0 0 0 1 1