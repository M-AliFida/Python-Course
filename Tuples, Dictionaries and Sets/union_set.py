# Union operation on both sets produces a new set 
# With all distinct elements

numbers_one = set([1, 2, 3])
numbers_two = set([1, 2, 3, 4, 5, 6])

my_numbers = numbers_one | numbers_two
print(my_numbers)

# {1, 2, 3, 4, 5, 6} 