# Given a random integer array, push all the zeros that are present to end of the array. 
# The respective order of other elements should remain same.

n = int(input())
lis =list(map(int, input().split()))
for i in lis:
    if i != 0:
        print(i, end = " ")
x = lis.count(0)
print("0 " * x)

# 6
# 0 3 2 0 0 9
# 3 2 9 0 0 0 