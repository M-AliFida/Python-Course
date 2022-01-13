# Given a random integer array(ARR) and a number X. 
# Find and print the pair of elements in the array which sum to X.
# Given array can contain duplicate elements as well.
# While printing a pair, print the smaller element first.
# That is, if a valid pair is (6, 5) print "5 6". 

def pair_sum(x , y):
    if x <= y:
        print(x, " ", y)
    else:
        print(y, " ", x)
        
n = int(input())
lis = [int(x) for x in input().split()[:n]]
sum = int(input())
for i in range(0, len(lis) - 1):
    for j in range(i + 1, len(lis)):
        if(lis[i] + lis[j] == sum):
            pair_sum(lis[i], lis[j])

# 2 4 6 4 3 2
# 8
# 2   6
# 4   4
# 2   6