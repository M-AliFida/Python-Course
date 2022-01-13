# Given an array
# Sort the array

n = int(input("Enter size of array: "))
lis = [int(x) for x in input().split()[:n]] 

for i in range(0, len(lis) - 1):
    min = lis[i]
    for j in range(i + 1, len(lis)):
        if min > lis[j]:
            min = lis[j]
            lis[i], lis[j] = lis[j], lis[i]

for x in lis:
    print(x, end = ' ')

# Enter size of array: 5
# 5 4 3 2 1
# 1 2 3 4 5