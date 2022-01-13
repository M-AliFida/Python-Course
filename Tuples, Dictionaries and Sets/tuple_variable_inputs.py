# Using tuples to give a variable number of inputs and printing them

def tuple_print_num(x, y, *more):
    print(x)
    print(y)
    print(more)

tuple_print_num(1, 2, 3, 4, 5)

# 1 -- x
# 2 -- y
# (3, 4, 5) -- more