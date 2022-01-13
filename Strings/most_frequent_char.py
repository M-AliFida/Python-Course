# Given a string, S, find and return the highest occurring character present in the given string.
# If there are 2 characters in the input string with same frequency, return the character which comes first.
# Assume all the characters in the given string are lowercase.

def frequent_char(string_frequent):
  aschii = 256
  chr = [0] * aschii
  max = -1
  char = ''
  for i in string_frequent:
    chr[ord(i)] += 1 
 
  for i in string_frequent:
    if max < chr[ord(i)]:
      max = chr[ord(i)]
      char = i
  return char

string_frequent =input()
print(frequent_char(string_frequent))

# ababbcd
# b

# abaabbcd
# a
# N.B. a comes before b so it is printed