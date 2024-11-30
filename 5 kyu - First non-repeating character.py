# Write a function named first_non_repeating_letter† that takes a string input, 
# and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't', 
# since the letter t only occurs once in the string, and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same character, 
# but the function should return the correct case for the initial letter. For example, 
# the input 'sTreSS' should return 'T'.

# If a string contains all repeating characters, it should return an empty string ("");

# † Note: the function is called firstNonRepeatingLetter for historical reasons, 
# but your function should handle any Unicode character.

def first_non_repeating_letter(s):
     string_lower = s.lower()
     for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return s[i]
            
     return ""

print(first_non_repeating_letter('hLlKG1zSx;uyf,nqUWfU3 YAxQQfes0i 67Hv:1X9 IAiKpci3 QW OqX'))