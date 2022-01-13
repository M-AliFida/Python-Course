# 4
#    *   
#   ***  
#  ***** 
# *******


l = int(input())
p = '*'
for i in range(l):
    #rjust() and ljust() for right and left alligment respectively 
    print((p * i).rjust(l - 1) + p + (p * i).ljust(l - 1))