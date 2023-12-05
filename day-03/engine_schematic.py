def parse_file(filepath):

    engine_matrix = []
    with open(filepath, "r") as file:

        # add dot buffer
        # line_length = len(file[0])
        # first_line = ["."] * (line_length + 2)

        # engine_matrix.apend(first_line)

        for line in file:
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
                while padded_engine_matrix[y][end_index].isdigit():
                    end_index +=1

                if is_part_of_schema(padded_engine_matrix, y, start_index, end_index):
                    # convert to number
                    digits = padded_engine_matrix[y][start_index : end_index:]
                    part_number = int(''.join(digits))
                    print("part_number", part_number)
                    part_numbers.append(part_number)

                x = end_index
            x += 1

    return part_numbers

def is_part_of_schema(matrix, row_index, start_index, end_index):
    ...
    return True

