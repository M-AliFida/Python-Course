# Tuple is an ordered collection of elements/enteries
# Objects in a tuple are immutable
# Elements are placed within () and seperated by ,
# Elements can be of different data types

a = ("hello", "dear", "friend")
print(a)
print(type(a))

b = () # this is an empty tuple
print(b)

c  = ("single", )
print(c)
print(type(c)) # this is a tuple with a single element, we use a trailing comma.

slice_me = (1, 2, 3, 4, 5, 6)
print(slice_me[1 : 4]) # slicing a tuple

# slice_me[0] = 0
# TypeError: 'tuple' object does not support item assignment
# You cannot change any single element in tuple

slice_me = ([1,2], "hello", "there") # you can assign another tuple however
print(slice_me)

slice_me[0][0] = 0 # you can change mutable objects within the tuple
print(slice_me)

# del(slice_me) # to delete a tuple