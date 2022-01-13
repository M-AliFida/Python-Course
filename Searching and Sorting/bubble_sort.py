# Given a random integer array. Sort this array using bubble sort (simple sorting algorithm).
# Change in the input array itself. You don't need to return or print elements.

def bubbleSort(lis): 
    n = len(lis) 
    for i in range(n):
        for j in range(0, n - i - 1): 
            if lis[j] > lis[j + 1] : 
                lis[j], lis[j + 1] = lis[j + 1], lis[j] 
    print(* lis)

n = int(input())
array = list(map(int,input().split()))
bubbleSort(array)

# N = 5
# 5 4 3 2 1
# 1 2 3 4 5