# Ssing tuples to calculate sum of variable number of inputs

def tuple_variable_sum(x, y, *more):
    sum = x + y
    for i in more:
        sum += i
        
    return sum

output = tuple_variable_sum(1, 2, 3, 4, 5)
print(output)

#15