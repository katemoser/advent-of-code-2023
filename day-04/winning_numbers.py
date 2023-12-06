def parse_file(filepath):
    ...

    cards = []

    with open(filepath, "r") as file:
        for line in file:
            card_nums_string = line.split(":")[1]
            [winning_nums_string, scored_nums_string] = card_nums_string.split("|")

            winning_nums = [
                int(n) for n in winning_nums_string.strip().split(" ") if n]
            scored_nums = [
                int(n) for n in scored_nums_string.strip().split(" ") if n]

            cards.append([winning_nums, scored_nums])

    return cards


def score_card(card):
    ...

    [winning_nums, scored_nums] = card

    winning_nums.sort()
    scored_nums.sort()

    w_index = 0
    s_index = 0
    num_winning_nums = 0

    # count number of winning numbers on card
    while (w_index < len(winning_nums) and s_index < len(scored_nums)):
        if winning_nums[w_index] == scored_nums[s_index]:
            num_winning_nums += 1
            s_index += 1
        elif winning_nums[w_index] < scored_nums[s_index]:
            w_index += 1
        else:
            s_index += 1

    return 2**(num_winning_nums -1) if num_winning_nums > 0 else 0

def parse_file_and_sum_scores(filepath):
    ...
    cards = parse_file(filepath)

    total_score = 0

    for card in cards:
        total_score += score_card(card)

    print("total score is ", total_score)
    return total_score