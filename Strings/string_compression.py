# Write a program to do basic string compression. 
# For a character which is consecutively repeated more than once
# Replace consecutive duplicate occurrences with the count of repetitions.
# For e.g. if a String has 'x' repeated 5 times, replace this "xxxxx" with "x5".

def compression(string_c):
    i = 0
    x = ''
    while(i < len(string_c)):
        j = i + 1
        c = 1
        while j<len(string_c) and (string_c[i] == string_c[j]):
            j += 1
            c += 1
        if c == 1:
            x += string_c[i]
        else:
            x += string_c[i]+ str(c)
        i = j
    return x

string_c = input()
print(compression(string_c))

# aaabbc
# a3b2c