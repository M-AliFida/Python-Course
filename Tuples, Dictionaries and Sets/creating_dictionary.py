# Associative array
# Unordered collection of key-value pairs
# Use of {key: value}
# Keys must be unique and of mutable data type
# Values do not need to be unique and can be immutable
# Dictionaries themselves are mutable

sample_dict = {1 : 2, "hello" : "bye"} # creating a dictionary
weekend = {5: "Saturday", 6 : "Sunday"}

my_list = [("a", 1), ("b", 2)] # type cast a list into a dictionary although this must be a list of typles of length 2.
my_dictionary = dict(my_list)
print(my_dictionary)

# {'a': 1, 'b': 2}

my_copied_dictionary = my_dictionary.copy() # duplicating dictionary
print(my_copied_dictionary)

# {'a': 1, 'b': 2}

other_dictionary = dict.fromkeys(["key_1", "key_2", "key_3"], "same_value")
print(other_dictionary) #using fromKeys-- variable keys with the same value

# {'key_1': 'same_value', 'key_2': 'same_value', 'key_3': 'same_value'}

print(other_dictionary.keys()) # accessing keys

# dict_keys(['key_1', 'key_2', 'key_3'])

print(other_dictionary.values()) # accessing values

# dict_values(['same_value', 'same_value', 'same_value'])

print(other_dictionary.items()) # accessing both key-value pairs

# dict_items([('key_1', 'same_value'), ('key_2', 'same_value'), ('key_3', 'same_value')])

# other_dictionary.clear # deleting all enteries from the dictionary
# print(other_dictionary) 