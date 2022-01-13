# Write a Program to determine if the given number is Armstrong number or not. 
# Print true if number is armstrong, otherwise print false.
# An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.
# For example,
# 371, as 3^3 + 7^3 + 1^3 = 371
# 1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634

def armstrong_number(n):
    exp = 0
    temp = n
    while temp > 0:
        temp = temp // 10
        exp = exp + 1
    arm_num = 0
    while n > 0:
        rem = n % 10
        arm_num = arm_num + rem ** exp
        n = n // 10
    return arm_num

n = int(input())
x = armstrong_number(n)
if n == x:
    print("true")
else:
    print("false")

# 1634
# true