def sum(a, b, c = 0):   # c = 0 by default
    print("c =", c)
    return a + b + c

print(sum(2, 3, 4)) # default value can be changed

# c = 4
# 9

print(sum(3, 4))

# c = 0
# 7