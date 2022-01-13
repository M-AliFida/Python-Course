# Using set to return sum of unique numbers

def sum_unique_set(l):
    s = set()
    for i in l:
        s.add(i)
    sum = 0
    for i in s:
        sum += i
    return sum

my_sum = sum_unique_set([1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 5, 6, 7, 8, 9])
print(my_sum)

# 45 -- 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9