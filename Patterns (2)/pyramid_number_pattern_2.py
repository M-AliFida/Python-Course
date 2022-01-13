# 4
#    1
#   232
#  34543
# 4567654

n = int(input())
row = 1
while row <= n:
    s = 1
    while s <= (n - row) :
        print(" ", end = "")
        s += 1
    column = 1
    p = row
    while column <= row :
        print(p, end = "")
        p += 1
        column += 1
    column = 1
    p = 2 * row - 2 
    while column <= row - 1 :
        print(p, end = "")
        p -= 1
        column += 1 
    print()
    row += 1
