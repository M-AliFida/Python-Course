# Write a program that works as a simple calculator. It reads an integer for choice.
# 1. If the choice is 1, 2 integers are taken for input and their sum is printed.
# 2. If the choice is 2, 2 integers are taken for input and their difference is printed.
# 3. If  the choice is 3, 2 integers are taken for input and their product is printed.
# 4. If  the choice is 4, 2 integers are taken for input and their quotient is printed.
# 5. If  the choice is 5, 2 integers are taken for input and their remainder is printed.
# 6. If the choice is 6, the program exits, 
# For any other choice, print "Invalid Operation" and ask for choice again.

n = int(input())
while n != 6:
    if n <= 5 and n >= 1:
        a=int(input())
        b=int(input())
    if n == 1:
        print(a + b)
    if n == 2:
        print(a - b)
    if n == 3:
        print(a * b)
    if n == 4:
        print(a // b)
    if n == 5:
        print(a % b)
    elif n < 1 or n > 6:
        print("Invalid Operation")
    n = int(input())