# Given a String s, check it its palindrome. 
# Return true if string is palindrome, else return false.
# Palindrome strings are those, where string s and its reverse is exactly same.

s = input()
p = s[::-1]
if(s == p):
    print("true")
else:
    print("false")

# racecar
# true