# Function to search through array and return index number of number to search. 
# Given a sorted integer array (in ascending order) and an element "VAL". 
# You need to search this element "VAL" in the given input array using Binary Search. 
# Return the index of element in the input.
# Indexing starts from 0.

def binary_search(lis, low, high, find):
    if low <= high:
      mid = (low + high) // 2
      if find == lis[mid]:
        return mid
      elif lis[mid] > find:
        return binary_search(lis, low, mid - 1, find)
      elif lis[mid] < find:
        return binary_search(lis, mid + 1, high, find)
    else:
      return -1
        
n = int(input())        
lis = [int (x) for x in input().split() [:n]]
find = int(input())
x = binary_search(lis, 0, n - 1, find)
print(x)
      
# 4
# 2 4 8 6
# 8
# 2