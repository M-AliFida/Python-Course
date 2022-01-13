# Write a program to generate the reverse of a given number N. 
# Print the corresponding reverse number.

n = int(input())
rev = 0
while (n > 0):
    d = n % 10
    rev = rev * 10 + d
    n = n // 10
print(rev)

# 123
# 321