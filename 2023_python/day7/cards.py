import os


def parse_hands_data(hands):
    card_list = []

    for hand in hands:
        # create a dictionary to store the hand
        cards, card_score = hand.split()
        hand = {"cards": None, "score": int(card_score)}

        # get the poker hand
        hand_score = get_poker_hand(cards)
        hand["hand"] = hand_score

        # get the value of the cards
        cards = get_cards_value(cards)
        hand["cards"] = cards

        card_list.append(hand)

    return card_list


# function that returns the poker hand in current hand
def get_poker_hand(hand):
    poker_hands = {
        "5": 6,  # five of a kind
        "14": 5,  # four of a kind
        "23": 4,  # full house
        "113": 3,  # three of a kind
        "122": 2,  # two pair
        "1112": 1,  # one pair
        "11111": 0,  # high card
    }

    card_count = {}

    for card in hand:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1

    card_count = sorted(card_count.values())
    card_count = "".join(str(x) for x in card_count)

    poker_hand = poker_hands.get(card_count)

    return poker_hand


def get_cards_value(cards):
    card_value_map = {
        "2": "12",
        "3": "13",
        "4": "14",
        "5": "15",
        "6": "16",
        "7": "17",
        "8": "18",
        "9": "19",
        "T": "20",
        "J": "21",
        "Q": "22",
        "K": "23",
        "A": "24",
    }

    cards_value = ""

    for card in cards:
        value = card_value_map.get(card)
        cards_value += value

    return cards_value


def get_wins(hands):
    for hand in hands:
        hand["wins"] = 0

        for opposing_hand in hands:
            win = compare_hands(hand, opposing_hand)
            if win:
                hand["wins"] += 1

    return hands


def compare_hands(hand_1, hand_2):
    if hand_1["hand"] == hand_2["hand"]:
        if hand_1["cards"] > hand_2["cards"]:
            return True
    elif hand_1["hand"] > hand_2["hand"]:
        return True
    else:
        return False


def get_total_winnings(hands):
    total = 0

    for hand in hands:
        total += hand["score"] * (hand["wins"] + 1)

    return total


# file path
script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")

# open file and split lines
with open(input_file_path, encoding="utf-8") as file:
    data = file.read().splitlines()

# parse data
hands_list = parse_hands_data(data)
hands_list = get_wins(hands_list)

# calculate winnings
total_winnings = get_total_winnings(hands_list)

print(total_winnings)
