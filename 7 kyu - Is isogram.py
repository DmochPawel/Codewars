# An isogram is a word that has no repeating letters, 
# consecutive or non-consecutive. Implement a function that determines whether a string 
# that contains only letters is an isogram. Assume the empty string is an isogram. 
# Ignore letter case.

# Example: (Input --> Output)

def is_isogram(string):
    seen = []
    for char in string:
        if char.lower() not in seen:
            seen.append(char.lower())
        else:
            return False
    return True
   
           

    
print(is_isogram("Dermatoglyphics"))
print(is_isogram("isogram"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
print(is_isogram("isIsogram"))
print(is_isogram(""))
