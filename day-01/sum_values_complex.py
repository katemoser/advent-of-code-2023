
def read_file_and_add_calibration_values(filepath):
    """read file, get calibration values and add together"""

    sum = 0
    with open(filepath, "r") as file:
        for line in file:
            print("in main, line =", line)
            sum += decode_calibration_value(line)

    return sum

def decode_calibration_value(line):
    """
    find the first and last 'digit'
    a digit being either the string of a number or a digit
    combine the two, return as 2 digit int
    """

    words_to_string_digits = {
        "one" : "1",
        "two": "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six": "6",
        "seven" : "7",
        "eight" : "8",
        "nine": "9",
    }

    string_digits = "0123456789"

    # find first digit
    #check if there is a word digit before that first digit
        # if there is, looks up the word to get the string digit
        # if not, use first found digit
    # find second digit
    # check if there is a word digit after that last digit
        # if there is, look up for  string digit
        # if not,  use last found digit

    # first_digit_and_index = None
    # last_digit_and_index = None

    # for index in range(len(line) -1):
    #     if line[index] in string_digits:
    #         if first_digit_and_index == None:
    #             first_digit_and_index = (line[index], index)
    #             last_digit_and_index = (line[index], index)
    #         else:
    #             last_digit_and_index = (line[index], index)

    # print("first", first_digit_and_index, "last", last_digit_and_index)

    first_digit = None
    last_digit = None

    while first_digit == None:
        if line[0] in string_digits:
            first_digit = line[0]
            break

        for number_word in words_to_string_digits:
            if line.startswith(number_word):
                first_digit = words_to_string_digits[number_word]
                break

        if first_digit == None:
            line = line[1::]

    while last_digit == None:
        # print("finding last digit, line=", line)
        if line[len(line)-1] in string_digits:
            last_digit = line[len(line)-1]
            break

        for number_word in words_to_string_digits:
            # print("checking number_word", number_word)
            if line.endswith(number_word):
                last_digit = words_to_string_digits[number_word]
                break

        line = line[:len(line)-1:]

    print("firstdigit", first_digit)
    print("lastdigit", last_digit)

    return int(first_digit + last_digit)

