# Finds total number of vowels (a, e, i, o and u), consonants (any character not a vowel)
# Digits (1-9) and special characters (anything not covered in the other categories)

def string_analysis(str):
    vowels, consonants, digits, special = 0, 0, 0, 0
    for char in str:
        
        if((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')):
            char = char.lower()
            if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
                vowels += 1
            else:
                consonants += 1
        elif char >= '0' and char <= '9':
            digits += 1
        else:
            special += 1
    return vowels,consonants,digits,special
            
    

str = "aeiouzbvcnmdrr!!!&%$^@3748"

vowels, consonants, digits, special = string_analysis(str)
print("vowels:", vowels, "consonants:", consonants, "digits:", digits, "special:", special)

# vowels: 5 consonants: 9 digits: 4 special: 8