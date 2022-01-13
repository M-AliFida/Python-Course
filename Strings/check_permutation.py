# Given two strings, S and T, check if they are permutations of each other. 
# Return true or false.
# Permutation means - length of both the strings should same and should contain same set of characters. 
# Order of characters doesn't matter.

S = input()
T = input()
count_1 = []
count_2 = []

chars_1 = 26 # Number of chars
while chars_1:
    count_1.append(0)
    chars_1 -= 1
    
chars_2 = 26
while chars_2:
    count_2.append(0)
    chars_2 -= 1

def check_length(S, T):
    if len(S) != len(T):
        return 0
    else:
        return 1
    
def check_1(str):
    for i in str:
        ascii = ord(i)
        count_1[ascii % 97] += 1
    return count_1

def check_2(str):
    for i in str:
        ascii = ord(i)
        count_2[ascii % 97] += 1
    return count_2

if check_length(S, T):
    lis_1 = check_1(S)   
    lis_2 = check_2(T)
 
    flag = True
    for i in range(0, 26):
        if lis_1[i] != lis_2[i]:
            flag = False
    if flag == False:
        print("false")
    else:
        print("true")
    
else:
    print("false")

# hello
# olleh
# true
        
# abc
# bbb
# false
    