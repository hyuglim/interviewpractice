
def is_rotation(string_one, string_two):
    combined_string = string_one + string_two
    return string_one in combined_string or \
            string_two in combined_string


assert(is_rotation("waterbottle", "erbottlewat"))
