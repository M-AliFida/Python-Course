# Given a string S, reverse each word of a string individually. 
# For eg. if a string is "abc def", reversed string should be "cba fed".

def reverse_each_word(str):  
   word = str.split(" ")                         
   new_w = [i[::-1] for i in word]                 
   new_s = " ".join(new_w)
   return new_s

str = input()
print(reverse_each_word(str))

# love si evol
# evol is love