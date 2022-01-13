# Reverse elements in a list

def list_reversal(lis):
    length = len(lis)
    for i in range(length // 2):
        lis[i], lis[-i-1] = lis[-i-1], lis[i] 

lis = [1,2,3,4,5,6]
list_reversal(lis)
print(lis)

# [6, 5, 4, 3, 2, 1]