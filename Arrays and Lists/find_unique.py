# Given an integer array of size 2N + 1. 
# In this given array, N numbers are present twice and one number is present only once in the array.
# You need to find and return that number which is unique in the array.

n = int(input())
lis = list(map(int, input().split()))
x = list(set(lis))
for i in x:
    if lis.count(i) == 1:
        break
print(i)

# 6
# 1 1 2 2 2 4
# 4