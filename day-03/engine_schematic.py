def parse_file(filepath):

    engine_matrix = []
    with open(filepath, "r") as file:

        # add dot buffer
        # line_length = len(file[0])
        # first_line = ["."] * (line_length + 2)

        # engine_matrix.apend(first_line)

        for line in file:
            line = line.strip()
            matrix_row = ["."]
            for char in line:
                matrix_row.append(char)
                #
                # old code for reference
                # if char.isdigit():
                #     matrix_row.append(int(char))

                # elif char == ".":
                #     matrix_row.append(None)
                # else:
                #     matrix_row.append(char)

            matrix_row.append(".")
            engine_matrix.append(matrix_row)
    # add first and last lines
    line_length = len(engine_matrix)
    first_line = ["."] * (line_length + 2)
    last_line = ["."] * (line_length + 2)

    engine_matrix.insert(0, first_line)
    engine_matrix.append(last_line)

    print("paddedEngineMatrix:", engine_matrix)

    return engine_matrix

def read_file_and_find(filepath):

    padded_engine_matrix = parse_file(filepath)

    part_numbers = []

    for y in range(len(padded_engine_matrix)):

        x = 0
        while x < len(padded_engine_matrix[y]):
            # print("x", x, "y", y)

            if padded_engine_matrix[y][x].isdigit():
                start_index = x
                end_index = x

                # find end of number
                while (
                    padded_engine_matrix[y][end_index+1].isdigit()):

                    end_index +=1

                print("this is the indexs of the number:", start_index, end_index)

                if is_part_of_schema(padded_engine_matrix, y, start_index, end_index):
                    # convert to number
                    digits = padded_engine_matrix[y][start_index : end_index +1 :]
                    part_number = int(''.join(digits))
                    print("part_number", part_number)
                    part_numbers.append(part_number)

                x = end_index
            x += 1

    return part_numbers

def is_part_of_schema(matrix, row_index, start_index, end_index):
    i = start_index

    # anytime check up down and 4 diagonals
    chars_to_check = []
    while i <= end_index:
        # if start index, check left
        if i == start_index:
            chars_to_check.append(matrix[row_index][i-1])
            chars_to_check.append(matrix[row_index-1][i-1])
            chars_to_check.append(matrix[row_index+1][i-1])

        # if end index check right
        if i == end_index:
            print("end index", end_index)
            chars_to_check.append(matrix[row_index][i+1])
            chars_to_check.append(matrix[row_index-1][i+1])
            chars_to_check.append(matrix[row_index+1][i+1])

        chars_to_check.append(matrix[row_index-1][i])
        chars_to_check.append(matrix[row_index+1][i])

        i +=1
    print("chars to check:", chars_to_check)

    for char in chars_to_check:
        if not char.isdigit() and not char.isalpha() and char != ".":
            return True

    return False


def read_file_and_find_sum_of_gear_ratios(filepath):
    ...
    # read file and create padded engine
    padded_engine_matrix = parse_file(filepath)

    star_indexes = find_indexes_of_stars(padded_engine_matrix)

    gear_ratios = []
    for (y, x) in star_indexes:
        ratio = if_gear_find_gear_ratio(padded_engine_matrix, y, x)
        if ratio: gear_ratios.append(ratio)

    print("GEAR RATIOS", gear_ratios)

    sum = 0

    for ratio in gear_ratios:
        sum += ratio

    return sum

def find_indexes_of_stars(matrix):
    """returns list of y,x pairs as tuples of coords for asterisks"""

    star_indexes = []
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == "*":
                star_indexes.append( (y,x) )

    print("indexes:", star_indexes)
    return star_indexes

def if_gear_find_gear_ratio(matrix, row_idx, col_idx):
    ...
    # for each location around the star, check if unvisited digit.
    #   if it's an unvisited digit, visit all digits of this "number", add num to adjnums
    # if adj_nums length == 2 return product of two numbers, else None

    adj_nums = []
    visited_coords = []

    to_visit_coords = []

    # make list of coords around star
    to_visit_coords.append( (row_idx-1, col_idx-1))
    to_visit_coords.append( (row_idx-1, col_idx))
    to_visit_coords.append( (row_idx-1, col_idx+1))
    to_visit_coords.append( (row_idx, col_idx+1))
    to_visit_coords.append( (row_idx+1, col_idx+1))
    to_visit_coords.append( (row_idx+1, col_idx))
    to_visit_coords.append( (row_idx+1, col_idx-1))
    to_visit_coords.append( (row_idx, col_idx-1))

    for (y,x) in to_visit_coords:
        if (y,x) not in visited_coords:
            visited_coords.append( (y,x) )

            if matrix[y][x].isdigit():
                # find entire number, add to adj_nums
                start_index = x
                end_index = x

                while matrix[y][start_index-1].isdigit():
                    start_index -= 1
                    visited_coords.append( (y, start_index))

                while matrix[y][end_index + 1].isdigit():
                    end_index += 1
                    visited_coords.append( (y, end_index))

                digits = matrix[y][start_index : end_index +1 :]
                num = int(''.join(digits))
                print("num", num)
                adj_nums.append(num)

    print("adjacent numbers:", adj_nums)

    # if exactly 2 adjacent numbers, return product
    # else return None
    if len(adj_nums) == 2:
        return adj_nums[0] * adj_nums[1]
    else:
        return None



    return 1
