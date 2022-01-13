# N = 5
#   *
#  ***
# *****
#  ***
#   *

n = int(input())
first_half = (n + 1) // 2
second_half = n // 2

#First Half
row = 1 
while row <= first_half:
    s = 1 
    while s <= (first_half - row) :
        print(" ", end = "")
        s += 1
    column = 1
    while column <= (2 * row) - 1 :
        print("*", end = "")
        column += 1
        
    print()
    row += 1

#Second Half 
row = second_half 
while row >= 1 :
    s = 1
    while s <= (second_half - row + 1) :
        print(" ", end = "") 
        s += 1
    column = 1 
    while column <= (2 * row) - 1 :
        print("*", end = "") 
        column += 1
    
    print()
    row -= 1