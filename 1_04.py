# 1.4
# Write a method to replace all spaces in a string with '%20'. You may assume
# that the string has sufficient space at the end of the string to hold the
# additional characters, and that you are given the "true" length of the string

def replace_string(string):
    return '%20'.join(string.split())
