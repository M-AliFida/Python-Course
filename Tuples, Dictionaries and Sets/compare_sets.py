# We can compare sets to see if a given set is a subset or superset of another set
# True or False is printed

numbers_one = set([1, 2, 3])
numbers_two = set([1, 2, 3, 4, 5, 6])

my_numbers = numbers_one - numbers_two
print(my_numbers)

is_subset = numbers_one <= numbers_two
is_superset = numbers_two >= numbers_one
print(is_subset)
print(is_superset)

# True
# True