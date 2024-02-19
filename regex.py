import re

def search():
    pattern = "apple"
    text = "I love apples"
    result = re.search(pattern, text) #will have 3 params - index and which pattern starts, ends and .group() -> the actual pattern

def replace():
    pattern = "apple"
    replace = "pear"
    text = "I love apples"
    re.sub(pattern, replace, text) #will replace apple with pear

def repetition():
    #match repeated string with * or +
    #a* means 0 or more of a
    #a+ means 1 or more of a
    word = "aaaaaaaacccaabbbbaaaba"
    re.sub("a+", "f", word) #replace all a with f
    new_word = re.sub("a*c", "d", word) #replace any occurance of c

''' 
We also have special characters
# . -> wildcard (any character)
# \b -> word boundary
# \s -> whitespace character
# \d -> digit
# \w -> word character (a-z, A-Z, 0-9, _)

If you capatalise these, it is negation
'''