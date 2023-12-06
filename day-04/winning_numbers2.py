


def parse_file(filepath):
    ...
    cards = {}

    with open(filepath, "r") as file:
        for line in file:
            [card_title, card_nums_string] = line.split(":")
            card_num = int(card_title.split(" ")[-1].strip())

            [winning_nums_string, scored_nums_string] = card_nums_string.split("|")

            winning_nums = [
                int(n) for n in winning_nums_string.strip().split(" ") if n]
            scored_nums = [
                int(n) for n in scored_nums_string.strip().split(" ") if n]

            cards[card_num] = [winning_nums, scored_nums]
            # cards.append([winning_nums, scored_nums])

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

    return num_winning_nums

def calculate_num_scratch_cards(filepath):

    cards = parse_file(filepath)

    num_cards = {card_num : 1 for card_num in cards.keys()}

    print(num_cards)

    for card_num in cards:
        num_winning_nums = score_card(cards[card_num])
        num_instances_of_card = num_cards[card_num]

        for n in range(card_num +1, card_num +1 +num_winning_nums ):
            num_cards[n] += num_instances_of_card


    print(num_cards)
    total_num_cards = 0
    for n in num_cards.values():
        total_num_cards += n

    print(f"you have {total_num_cards} cards, total")
    return total_num_cards