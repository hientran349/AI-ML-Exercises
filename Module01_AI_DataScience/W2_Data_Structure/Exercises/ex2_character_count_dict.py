def characterCountDict(str):
    result_dict = {} # empty dictionary
    # str = str.lower() # convert string to lowercase

    for ch in str: # go through all characters of the string

        # Add/Update the item in the dictionary
        #  result_dict.get(ch, 0): get current value (default is 0 if not found)
        result_dict[ch] =  result_dict.get(ch, 0) + 1

    print(result_dict)
    return result_dict


#TESTING
str = "Happiness"
characterCountDict(str)

str = "smiles"
characterCountDict(str)


# TRAC NGHIEM 2
assert characterCountDict("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(characterCountDict('smiles'))  # Output: {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
# Answer: a)