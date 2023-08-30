from collections import Counter

card1 = "A spades"
card2 = "5 spades"
hand = [card1, card2]
flop = ["2 spades", "7 clubs", "Q hearts", "J diamonds", "4 spades"]

# royal_flush
# straight_flush
# straight
# flush
# four_of_a_kind
# full_house
# three_of_a_kind
# two_pair
# one_pair
# high_card

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

def check_hand(flop, hand):
    all_cards = hand + flop
    print(all_cards)
    names = []
    suits = []
    for i in all_cards:
        x = i.split()
        names.append(x[0])
        suits.append(x[1])
    names_counter = Counter(names)
    suits_counter = Counter(suits)
    royal_flush = ["A", "K", "Q", "J", "10"]
    temp = []
    temp2 = []
    sorted_cards = sorted(names, key=lambda card: sequence[card])
    print(names)
    print(sorted_cards)
    print(suits)
    straight = False
    for i in range(len(sorted_cards) - 1):
        if sequence[sorted_cards[i]] == sorted_cards[i + 1]:
            straight = True
            index = names.index(sorted_cards[i])
            temp.append(suits[index])
    for i in names:
        for i2 in royal_flush:
            if i2 == i:
                index = names.index(i)
                temp2.append(suits[index])
    temp2 = list(dict.fromkeys(temp2))
    print(temp)
    print(temp2)
    print(names_counter.most_common)
    print(suits_counter.most_common)
    if len(temp2) == 5 and all(suit == temp2[0] for suit in temp2):
        return "Royal Flush"
    elif straight and all(suit == temp[0] for suit in temp):
        return "Straight Flush"
    elif straight:
        return "Straight"
    elif suits_counter.most_common(1)[0][1] >= 5:
        return "Flush"
    elif names_counter.most_common(1)[0][1] == 4:
        return "Four of a Kind"
    elif names_counter.most_common(1)[0][1] == 3 and names_counter.most_common(2)[1][1] == 2:
        return "Full House"
    elif names_counter.most_common(1)[0][1] == 3:
        return "Three of a Kind"
    elif names_counter.most_common(1)[0][1] == 2 and names_counter.most_common(2)[1][1] == 2:
        return "Two Pair"
    elif names_counter.most_common(1)[0][1] == 2:
        return "One Pair"
    else:
        return "High Card"

print(check_hand(flop, hand))
