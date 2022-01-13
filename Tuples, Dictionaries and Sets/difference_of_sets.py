# The difference operation on two sets produces a set
# Containing only elements from the first set and none from the second set


numbers_one = set([1, 2, 3, 0])
numbers_two = set([1, 2, 3, 4, 5, 6])

my_numbers = numbers_one - numbers_two
print(my_numbers)

# {0}