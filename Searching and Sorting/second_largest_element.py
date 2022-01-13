# Given a random integer array of size n, find and return the second largest element present in the array.
# If n <= 1 or all elements are same in the array, return -2147483648 i.e. -2^31.

n = int(input())
lis = [int(x) for x in input().split()[:n]]
lis.sort()
counter = 0
second_largest = 0
temp_max = 0

for i in range(0, len(lis) - 1):
  if lis[i] == lis[i + 1]:
    counter = counter + 1
  elif lis[i] > temp_max:
    temp_max = temp_max
    second_largest = lis[i]  

if (counter == n) or (n <= 1):
  print(-2147483648)
else:
  print(second_largest)

# 5
# 1 2 3 4 5
# 4