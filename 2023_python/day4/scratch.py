with open("2023_python/day4/input.txt", encoding="utf-8") as scratch_card_data:
    scratch_cards_data = scratch_card_data.read()
    scratch_cards_data = scratch_cards_data.splitlines()


def shape_scratch_card_data(data):
    cards = {}  # cards dict

    for card_data in data:
        card_id, numbers = card_data.split(":")  # split card id from nums
        win_nums, play_nums = numbers.split("|")  # split winning and played nums

        card_id = card_id.split()[1]  # "Card 12" -> "12"

        # add shaped card to cards dictionary
        cards[int(card_id)] = {
            "win_nums": set(win_nums.split()),
            "play_nums": set(play_nums.split()),
        }

    return cards


# compare winning and played card sets, return intersection count
def winning_numbers_count(wn, pn):
    return len(wn & pn)


# get total points for a winning card, doubled for each winning num
def get_points(win_count):
    points, i = 1, 1
    while i < win_count:
        points = points * 2
        i += 1

    return points


# score cards to get total points won
def score_cards(cards):
    total_points = 0
    for _, card in cards.items():
        win_count = winning_numbers_count(card["win_nums"], card["play_nums"])

        # don't calc points if no winning nums
        if win_count > 0:
            card_points = get_points(win_count)
            total_points += card_points

    return total_points


# count cards, duplicating ahead n times for n wins on current card
def count_cards(cards):
    card_count = 0
    dupes = {}

    for c_id, card in cards.items():
        win_count = winning_numbers_count(card["win_nums"], card["play_nums"])

        # dupes of this card plus this card
        instances = dupes.get(c_id, 0) + 1

        for _ in range(instances):  # for each instance of the current card
            for n in range(win_count):  # for each winning card
                i = n + 1

                # add a duplicate of card i spaces ahead
                if dupes.get(c_id + i):
                    dupes[c_id + i] += 1
                else:
                    dupes[c_id + i] = 1

            card_count += 1

    return card_count


scratch_cards = shape_scratch_card_data(scratch_cards_data)  # shaped data
SCRATCH_CARDS_POINTS = score_cards(scratch_cards)  # total points
SCRATCH_CARDS_COUNT = count_cards(scratch_cards)  # count cards

print("points: ", SCRATCH_CARDS_POINTS)
print("card count: ", SCRATCH_CARDS_COUNT)
