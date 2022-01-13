# Given a string, S, remove all the consecutive duplicates 
# That are present in the given string. 
# That means, if 'aaa' is present in the string then it should become 'a' in the output string.

str = input()
i = 0
non_dupl = ""
while i < len(str):
    x = str[i]
    j = i + 1
    c = 1
    while j<len(str) and str[j]==x:
        j = j + 1
    non_dupl += str[i]
    i = j
print(non_dupl)

# aaabbc
# abc