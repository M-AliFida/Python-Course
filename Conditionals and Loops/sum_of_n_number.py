# Given an integer n, find and print the sum of numbers from 1 to n.

n= int(input())
sum = 0
for i in range(n, 0, -1):
    sum = sum + i
print(sum)

# 10
# 55