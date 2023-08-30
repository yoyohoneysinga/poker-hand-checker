from collections import Counter

sequence = {
	"A": "2",
	"2": "3",
	"3": "4",
	"4": "5",
	"5": "6",
	"6": "7",
	"7": "8",
	"8": "9",
	"9": "10",
	"10": "J",
	"J": "Q",
	"Q": "K",
	"K": "A",
}

def check_royal_flush(names, suits):
    royal_flush = ["A", "K", "Q", "J", "10"]
    temp2 = []
    for i in names:
        for i2 in royal_flush:
            if i2 == i:
                index = names.index(i)
                temp2.append(suits[index])
    temp2 = list(dict.fromkeys(temp2))
    return len(temp2) == 5 and all(suit == temp2[0] for suit in temp2)

def check_straight_flush(sorted_cards, suits):
    straight_flush = False
    for i in range(len(sorted_cards) - 4):
        if all(sequence[sorted_cards[i + j]] == sorted_cards[i + j + 1] for j in range(4)):
            straight_flush = True
            break

    return straight_flush and check_flush(suits)

def check_straight(sorted_cards):
    sorted_cards = sorted(sorted_cards, key=lambda card: sequence[card])
    consecutive_count = 1

    for i in range(len(sorted_cards) - 1):
        if sequence[sorted_cards[i]] == sorted_cards[i + 1]:
            consecutive_count += 1
            if consecutive_count >= 5:
                return True
        else:
            consecutive_count = 1

    return False

def check_flush(suits):
    suits_counter = Counter(suits)
    return suits_counter.most_common(1)[0][1] >= 5

def check_four_of_a_kind(names):
    names_counter = Counter(names)
    return names_counter.most_common(1)[0][1] == 4

def check_full_house(names):
    names_counter = Counter(names)
    return names_counter.most_common(1)[0][1] == 3 and names_counter.most_common(2)[1][1] == 2

def check_three_of_a_kind(names):
    names_counter = Counter(names)
    return names_counter.most_common(1)[0][1] == 3

def check_two_pair(names):
    names_counter = Counter(names)
    return names_counter.most_common(1)[0][1] >= 2 and names_counter.most_common(2)[1][1] >= 2

def check_one_pair(names):
    names_counter = Counter(names)
    return names_counter.most_common(1)[0][1] >= 2

def check_hand(hand, flop):
    all_cards = hand + flop
    names = [x.split()[0] for x in all_cards]
    suits = [x.split()[1] for x in all_cards]
    sorted_cards = sorted(names, key=lambda card: sequence[card])

    royal_flush_hand = check_royal_flush(names, suits)
    straight_flush_hand = check_straight_flush(sorted_cards, suits)
    straight_hand = check_straight(sorted_cards)
    flush_hand = check_flush(suits)
    four_of_a_kind_hand = check_four_of_a_kind(names)
    full_house_hand = check_full_house(names)
    three_of_a_kind_hand = check_three_of_a_kind(names)
    two_pair_hand = check_two_pair(names)
    one_pair_hand = check_one_pair(names)

    return {
        "royal_flush": royal_flush_hand,
        "straight_flush": straight_flush_hand,
        "straight": straight_hand,
        "flush": flush_hand,
        "four_of_a_kind": four_of_a_kind_hand,
        "full_house": full_house_hand,
        "three_of_a_kind": three_of_a_kind_hand,
        "two_pair": two_pair_hand,
        "one_pair": one_pair_hand,
        "high_card": True
    }

card1 = "A spades"
card2 = "5 spades"
hand = [card1, card2]
flop = ["2 spades", "A clubs", "5 hearts", "A diamonds", "4 spades"]

hand_result = check_hand(hand, flop)
for hand_type, is_present in hand_result.items():
    print(f"{hand_type.capitalize().replace('_', ' ')}: {is_present}")
