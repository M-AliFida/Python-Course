# Given a random integer array(ARR) and a number X. 
# Find and print the triplets of elements in the array which sum to X.
# While printing a triplet, print the smallest element first.
# That is, if a valid triplet is (6, 5, 10) print "5 6 10". 

def triplet_sum(x, y, z):
    collection_lis = []
    collection_lis.append(x)
    collection_lis.append(y)
    collection_lis.append(z)
    collection_lis.sort()
    for element in collection_lis:
        print(element, end = ' ')
    print()
        
n = int(input())
lis = [int(x) for x in input().split()[:n]]
sum = int(input())
for i in range(0, len(lis) - 2):
    for j in range(i + 1, len(lis) - 1):
        for k in range(j + 1, len(lis)):
            if(lis[i] + lis[j] + lis[k] == sum):
               triplet_sum(lis[i], lis[j], lis[k])

# 10
# 1 2 3 4 5 6 7 8 9 10
# 15
# 1 4 10 
# 1 5 9 
# 1 6 8 
# 2 3 10 
# 2 4 9 
# 2 5 8 
# 2 6 7 
# 3 4 8 
# 3 5 7 
# 4 5 6