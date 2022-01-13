# Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
# Note : For printing multiple values in one line, put them inside print separated by space.
# You can follow this syntax for printing values of two variables val1 and val2 separated by space -
# print(val1, " ", val2)

n = int(input())
even = 0
odd = 0
while(n > 0):
    r = n % 10
    if(r % 2 == 0):
        even = even + r
    else:
        odd = odd + r
    n = n // 10
print(even , "and" , odd)

# 5212
# 4 and 6