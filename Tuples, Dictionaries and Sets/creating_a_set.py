# Set is a collection of item in no particular order
# Elements in a set cannot be repeated
# Elements in a set are immutable but the set as a whole is mutable
# Sets do not support indexing or slicing
# Typically used for mathematical operations like union, intersection, difference and complement, etc.

weekdays = set(["Mon", "Tue", "Wed", "Thur", "Fri" ]) # creating a set
weekends = {"Sat", "Sun"}
print(weekdays)
print(weekends)

# {'Fri', 'Tue', 'Wed', 'Thur', 'Mon'}
# {'Sun', 'Sat'}

# order of elements has changed ^

for x in weekdays: # accessing values, cannot access individual values as there is no specific order
    print(x)

# Mon
# Wed
# Tue
# Thur
# Fri

# add and removing items
weekdays.add("Another weekday?")
print(weekdays)
weekdays.remove("Another weekday?")
print(weekdays)

# {'Mon', 'Fri', 'Wed', 'Another weekday?', 'Thur', 'Tue'}
# {'Mon', 'Fri', 'Wed', 'Thur', 'Tue'}
