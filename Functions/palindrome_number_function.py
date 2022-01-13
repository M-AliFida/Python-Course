# Same exercise as in Conditionals and Loops with functions implementation
# Write a program to determine if given number is palindrome or not. 
# Print true if it is palindrome, false otherwise.

def reverse(n):  # returns the reverse of a number
    rev = 0
    while(n > 0):
        r = n % 10
        rev = (rev * 10) + r
        n = n // 10
    return rev 

def check_palindrome(num):
    rev_number = reverse(num)
    if rev_number == num:
        return 1 # true
    else:
        return 0 # false
    
		
n = int(input())
is_palindrome = check_palindrome(n)
if(is_palindrome):
	print('true')
else:
	print('false')

# 164461
# true
