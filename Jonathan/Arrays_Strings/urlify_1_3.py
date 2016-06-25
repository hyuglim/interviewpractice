# replace all spaces in a string with '%20'

def urlify(my_string):
    new_string = ""
    for char in my_string:
        if char == ' ':
            new_string += "%20"
        else:
            new_string += char
    return new_string


def urlify_in_place(char_array, replacement):
    index = 0
    while index < len(char_array):
        if char_array[index] == ' ':
            insert_replacement(char_array, replacement, index)
            index += len(replacement)
        else:
            index += 1
    return ''.join(char_array)


def insert_replacement(char_array, replacement, index):
    char_array[index] = replacement[0]
    for i in xrange(1, len(replacement)):
        char_array.insert(index + i, replacement[i])

    
sample = urlify_in_place([char for char in 'Mr John Smith   '], '%20')
print sample
assert(sample  ==  'Mr%20John%20Smith%20%20%20')
