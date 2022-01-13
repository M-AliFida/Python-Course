# Given two random integer arrays(ARR1 and ARR2) of size M and N. 
# You need to print their intersection; 
# That is, an intersection is defined when both the arrays contain a particular value 
# Or to put it in other words when there is a common value in both the arrays.

n = int(input()) 
lis_1 = [int(x) for x in input().split()[:n]] 
m = int(input()) 
lis_2 = [int(x) for x in input().split()[:m]] 
overlapping_lis = [] 

for i in lis_1:
   for j in lis_2:
      if i == j:
        overlapping_lis.append(i) 
        lis_2.remove(j) 
        break 

for x in overlapping_lis:
   print(x, end = "")

# 5
# 1 2 3 4 5
# 3
# 1 2 3