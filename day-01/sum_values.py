
def read_file_and_add_calibration_values(filepath):
    """read file, get calibration values and add together"""

    sum = 0
    with open(filepath, "r") as file:
        for line in file:
            print("in main, line =", line)
            sum += decode_calibration_value(line)

    return sum

def decode_calibration_value(line):
    """finds calibration value within one string"""

    digits = "1234567890"

    calibration_value = ""

    # get first digit as string
    for char in line:
        if char in digits:
            calibration_value += char
            break
    # get last digit as string

    for char in line[::-1]:
        if char in digits:
            calibration_value += char
            break
    # combine into two digit string, convert to number and return

    print("calibration value as string:", calibration_value)
    return int(calibration_value)
