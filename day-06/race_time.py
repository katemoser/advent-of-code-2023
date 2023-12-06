def parse_file(filepath):
    """
    take input like:
        Time:        56     97     78     75
        Distance:   546   1927   1131   1139
    return like [ [56, 546], [97, 1927], [78, 1131], [75, 1139] ]

    ...
    """

    ...


def calculate_num_ways_to_win(time_and_distance):

    [time, record_distance] = time_and_distance

    num_ways_to_win = 0

    for seconds_charging in range(time + 1):
        mps = seconds_charging
        time_racing = time - seconds_charging

        if mps * time_racing > record_distance:
            num_ways_to_win +=1

    print(num_ways_to_win)
    return num_ways_to_win

