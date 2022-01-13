# We can use a dictionary to help print
# Repetitive words that have frequency f

def print_f_frequent_words(string, f):
    words = string.split()
    my_dict = {}
    for w in words:
        my_dict [w] = my_dict.get(w , 0) + 1
    for w in my_dict:
        if my_dict[w] == f:
            print(w)

print_f_frequent_words("this and that and this and that", 2)

# this
# that

# both these words appear twice (f = 2)
