# Given an integer array, which is sorted (in increasing order) and has been rotated by some number k in clockwise direction. 
# Find and return the k.

def Rotate(lis, d = 1):
    if len(lis) == 0:
        return 1
    d = -d % len(lis)
    return lis[d:] + lis[:d]

n = int(input())
lis = list(int(i) for i in input().strip().split(' '))
temp_array  = []
for i in lis:
    temp_array.append(i)
    
for k in range(0, len(lis)):
    temp_array.sort()
    rotated = Rotate(temp_array, k)
    flag = True
    for i in range(0, len(rotated)):
        if rotated[i] == lis[i]:
            pass
        else:
            flag = False
            break
    if flag == True:
        print(k)
        break

# 6
# 15, 18, 2, 3, 6, 12
# 2

# Note. This may appear confusing at first
# The key is to note that the array is supposed to be sorted (in increasing order)
# The above array therefore was intially 2, 3, 6, 12, 15, 18
# Therefore it has rotated twice (2) clockwise. 