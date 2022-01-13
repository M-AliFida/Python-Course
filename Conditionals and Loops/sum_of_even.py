# Given a number N, print sum of all even numbers from 1 to N.

n = int(input())
sum = 0
for i in range(n, 0, -1):
    if(i % 2 == 0):
        sum = sum + i
print(sum)

# 10
# 30