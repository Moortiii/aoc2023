from collections import Counter, defaultdict
from functools import cmp_to_key

from solver import utils

POSSIBLE_CARDS = "AKQT98765432J"


def sort_hands(hand_a: tuple[str, str, int], hand_b: tuple[str, str, int]):
    for card_a, card_b in zip(hand_a[1], hand_b[1]):
        if POSSIBLE_CARDS.index(card_a[0]) < POSSIBLE_CARDS.index(card_b[0]):
            return 1
        elif POSSIBLE_CARDS.index(card_a[0]) > POSSIBLE_CARDS.index(card_b[0]):
            return -1

    return 0


def sort_occurences(a: tuple[str, int], b: tuple[str, int]):
    if a[1] > b[1]:
        return 1
    elif a[1] < b[1]:
        return -1

    if POSSIBLE_CARDS.index(a[0]) < POSSIBLE_CARDS.index(b[0]):
        return 1
    elif POSSIBLE_CARDS.index(a[0]) > POSSIBLE_CARDS.index(b[0]):
        return -1

    return 0


def solve(input_file: str):
    lines = utils.read_lines(input_file)

    category_to_func = {
        "five_of_a_kind": lambda hand: sorted(Counter(hand).values()) == [5],
        "four_of_a_kind": lambda hand: sorted(Counter(hand).values()) == [1, 4],
        "full_house": lambda hand: sorted(Counter(hand).values()) == [2, 3],
        "three_of_a_kind": lambda hand: sorted(Counter(hand).values()) == [1, 1, 3],
        "two_pair": lambda hand: sorted(Counter(hand).values()) == [1, 2, 2],
        "one_pair": lambda hand: sorted(Counter(hand).values()) == [1, 1, 1, 2],
        "high_card": lambda _: True,
    }

    hands = defaultdict(list)

    for line in lines:
        hand, bid = line.split()

        occurences = Counter([c for c in hand if c != "J"]).most_common()
        occurences = sorted(occurences, key=cmp_to_key(sort_occurences))

        original_hand = hand

        if len(occurences) > 0:
            hand = hand.replace("J", occurences[-1][0])

        for category, func in category_to_func.items():
            if func(hand):
                hands[category].append((hand, original_hand, bid))
                hands[category].sort(key=cmp_to_key(sort_hands))
                break

    winnings = 0
    current_rank = 1

    for category in list(category_to_func.keys())[::-1]:
        for hand in hands[category]:
            hand, original_hand, bid = hand
            winnings += int(bid) * current_rank
            current_rank += 1

    return winnings
