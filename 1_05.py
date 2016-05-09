###############################################################################
# 1.5
# Implement a method to perform basic string compression using the counts of
# repeated characters. For example, the string aabcccccaaa would become 
# a2b1c5a3. If the "compressed" string would not become smaller than the 
# original string, your method should return the original string.
###############################################################################

def string_compression(string):
    
    # create extra array for repetition counts
    count = [0] * (len(string) + 1)
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count[i]  = 1

    # count the occurences of the following characters
    counted_ones = []
    for i in range(0, len(count) - 1):
        if count[i] == 0:
            j = 1
            while count[i + j] != 0:
                j += 1
            counted_ones.append(j)

    # join each character with its count 
    string += ' '
    output = ''    
    j = 0    
    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            output += string[i] + str(counted_ones[j])
            j += 1
    
    # determine whether original string should be returned
    string = ''.join(string.split())
    if len(string) < len(output):
        return string
    else:
        return output
