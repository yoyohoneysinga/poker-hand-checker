from collections import Counter
import numpy

cards = {
    "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13,
}

def check_straight(sorted_cards):
    for i in range(len(sorted_cards) - 4):
        if all(sorted_cards[i + j] + 1 == sorted_cards[i + j + 1] for j in range(4)):
            return True
    return False

def check_hand(cards):
    all_cards_2 = [card[0] for card in cards]
    all_cards_3 = [card[1] for card in cards]

    a = Counter(all_cards_2)
    b = Counter(all_cards_3)

    sorted_cards = sorted(cards, key=lambda x: cards[x])

    if all(card in all_cards_2 for card in ['A', 'K', 'Q', 'J', '10']) and len(set(all_cards_3)) == 1:
        return "Royal Flush"
    elif check_straight(sorted_cards) and len(set(all_cards_3)) == 1:
        return "Straight Flush"
    elif check_straight(sorted_cards):
        return "Straight"
    elif len(set(all_cards_3)) == 1:
        return "Flush"
    elif a.most_common(1)[0][1] == 4:
        return "Four of a kind"
    elif a.most_common(2)[0][1] == 3 and a.most_common(2)[1][1] == 2:
        return "Full House"
    elif a.most_common(1)[0][1] == 3:
        return "Three of a kind"
    elif a.most_common(2)[0][1] == 2:
        if a.most_common(2)[1][1] == 2:
            return "Two Pair"
        else:
            return "One Pair"
    else:
        return "High Card"

def find_winner(hands, flop):
    ranked_hands = [(hand, check_hand(hand + flop)) for hand in hands]
    ranked_hands.sort(key=lambda x: -max(cards[c] for c in x[0]))

    return ranked_hands

q = input("Are you finding the best hand (1) or the winner (2): ")

if q == "1":
    hand = []
    for _ in range(2):
        card = input("Enter card: ")
        suit = input("Enter suit: ")
        hand.append((card, suit))
    
    flop = []
    for x in range(5):
        flop_card = input(f"Enter card {x+1}: ")
        flop.append((flop_card, ""))  # Empty suit since it's not used
    
    print(check_hand(hand + flop))
elif q == "2":
    hands = []
    players = int(input("How many players: "))
    for i in range(players):
        player_hand = []
        for _ in range(2):
            card = input(f"Enter player {i+1} card: ")
            suit = input(f"Enter player {i+1} suit: ")
            player_hand.append((card, suit))
        hands.append(player_hand)
    
    flop = []
    for x in range(5):
        flop_card = input(f"Enter card {x+1}: ")
        flop.append((flop_card, ""))  # Empty suit since it's not used
    
    winners = find_winner(hands, flop)
    for i, (hand, result) in enumerate(winners, start=1):
        print(f"Winner {i}: Hand: {hand}, Result: {result}")
