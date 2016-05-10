###############################################################################
# 1.1
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
###############################################################################

def has_unique_characters1(string):
    unique_chars = []
        
    for character in string:
        if character not in unique_chars:
            unique_chars.append(character)
                
    if len(unique_chars) == len(string):
        return True
    else:
        return False

# Without additional data structure:
def has_unique_characters2(string):
    
    j = 0
    for i in range(len(string) - 1):
        if string[i] not in string[i+1:]:
            j += 1
    if j + 1 == len(string):
        return True
    else:
        return False
