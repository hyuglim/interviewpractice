

word_to_digit = {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9
        }


def replace_digit_words_with_numbers(string):
    for word, digit in word_to_digit.iteritems():
        string = string.replace(word, str(digit))
    return string


def capture_multidigit(string):
    digits = [str(digit) for digit in range(10)]
    string_without_digits = ''
    curr_buffer = ''
    multiplier = 1
    for curr_char in string:
        if curr_char in digits:
            curr_buffer += curr_char
            multiplier = int(curr_buffer)
        else:
            string_without_digits += multiplier * curr_char
            curr_buffer = ''
            multiplier = 1
    return string_without_digits
            


def test_with_string(input_string, expected_string):
    assert(capture_multidigit(replace_digit_words_with_numbers(input_string)) == expected_string)

test_with_string('sevenabsixde', 'aaaaaaabdddddde')
test_with_string('onezeroxoney', 'xxxxxxxxxxy')

