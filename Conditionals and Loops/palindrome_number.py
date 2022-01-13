# Write a program to determine if given number is palindrome or not. 
# Print true if it is palindrome, false otherwise.

n = int(input())

reverse = 0
temp = n

while(temp > 0):
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
 

if(n == reverse):
    print("true")
else:
    print("false")

# 164461
# true