# Find sum of two arrays
# Treating arrays as two integers
# Add sum result in another array, outputting single digit at each index

def sum_of_arrays(array_1, array_2, n, m):
   flag = False
   res = []
   if n > m:
       size = n - m
       for i in range(size):
           array_2.insert(i, 0)
           
   else:
       size = m - n
       for i in range(size):
           array_1.insert(i, 0)
           
   size = len(array_1)
   
   for i in range(size -1, -1, -1):
       sum = array_1[i] + array_2[i]
       
       if flag:
           sum += 1
           
       if sum >= 10:
           flag = True
           curr_x = sum % 10
           res.append(curr_x)
           
       else:
           res.append(sum)
           flag = False
           
   else:
       if flag:
           res.append(1)
   
   if len(res) != size + 1:
       res.append(0)
   for x in res[::-1]:
       print(x, end = ' ')
           
   
n = int(input())
array_1 = [int(x) for x in input().split()[:n]]

m = int(input())
array_2 = [int(x) for x in input().split()[:m]]

sum_of_arrays(array_1, array_2, n, m)

# 4
# 4 4 4 4
# 3 
# 3 3 3
# 0 4 7 7 7 

# i.e. 4444 + 333 = 4777