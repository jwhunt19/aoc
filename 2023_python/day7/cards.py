import os
import copy


# parse hands data into a list of hand dictionaries
def parse_hands_data(hands_data):
    hands = []

    for hand in hands_data:
        # create a dictionary to store the hand
        cards, card_bid = hand.split()
        hand = {"cards": None, "bid": int(card_bid)}

        # get the poker hand
        hand_bid = get_poker_hand(cards)
        hand["hand"] = hand_bid

        # get the value of the cards
        cards = get_cards_value(cards)
        hand["cards"] = cards

        hands.append(hand)

    return hands


# returns poker hand value of current hand
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

    # count instances of each card
    card_counts = {}
    for card in hand:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1

    # get best possible hand if jokers are enabled
    if JOKERS and card_counts.get("J"):
        poker_hand = joker_hands(card_counts, poker_hands)
    else:
        poker_hand_string = get_poker_hand_string(card_counts)
        poker_hand = poker_hands.get(poker_hand_string)

    return poker_hand


# returns best possible hand with jokers
def joker_hands(card_count, poker_hands):
    j = card_count["J"]

    possible_hands = []

    for card, count in card_count.items():
        if not card == "J":
            hand = copy.deepcopy(card_count)
            hand[card] = count + j
            del hand["J"]
            possible_hands.append(hand)
        else:
            possible_hands.append(card_count)

    possible_hands = [get_poker_hand_string(hand) for hand in possible_hands]

    best_hand = -1
    for hand in possible_hands:
        hand_val = poker_hands[hand]
        if hand_val > best_hand:
            best_hand = hand_val

    return best_hand


# returns a string of card counts
def get_poker_hand_string(card_counts):
    poker_hand_string = sorted(card_counts.values())
    poker_hand_string = "".join(str(x) for x in poker_hand_string)
    return poker_hand_string


# returns arbitrary value of the cards
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
        "Q": "22",
        "K": "23",
        "A": "24",
    }

    # joker replaces jack, becomes weakest card
    if JOKERS:
        card_value_map["J"] = "11"
    else:
        card_value_map["J"] = "21"

    # get value of cards based on card_value_map
    cards_value = ""
    for card in cards:
        value = card_value_map.get(card)
        cards_value += value

    return cards_value


# returns win count for each hand for ranking
def get_wins(hands):
    for hand in hands:
        hand["wins"] = 0

        for opposing_hand in hands:
            win = compare_hands(hand, opposing_hand)
            if win:
                hand["wins"] += 1

    return hands


# returns True if hand_1 wins, False otherwise
def compare_hands(hand_1, hand_2):
    if hand_1["hand"] == hand_2["hand"]:  # tie breaker
        if hand_1["cards"] > hand_2["cards"]:  # compare card values
            return True
    elif hand_1["hand"] > hand_2["hand"]:
        return True
    else:
        return False


# returns sum of all each hand's (bid * wins)
def get_total_winnings(hands):
    total = 0

    for hand in hands:
        total += hand["bid"] * (hand["wins"] + 1)

    return total


# file path
script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, "input.txt")

# open file and split lines
with open(input_file_path, encoding="utf-8") as file:
    data = file.read().splitlines()

# joker flag (for part 2)
JOKERS = True

# parse data
hands_list = parse_hands_data(data)
hands_list = get_wins(hands_list)

# calculate winnings
total_winnings = get_total_winnings(hands_list)

print(total_winnings)
