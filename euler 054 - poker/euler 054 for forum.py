CARDS = "23456789TJQKA"
CARDS_VALUES = dict(zip(CARDS, range(2,15)))
POKER = ['Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight', 'Three of a Kind', 'Two Pairs', 'One Pair', 'High Card']

class PlayerHand:
    def __init__(self, cards):
        self.values  = sorted ( [CARDS_VALUES[i[0]] for i in cards] )
        self.suits   = set    ( [i[1] for i in cards] )
        self.counted = self.count_cards()
        self.rest_cards = {}

    def count_cards(self):
        result = {}
        for val in self.values:
            result[val] = result.get(val, 0) + 1
        return result

    def is_high_card(self):
        return 1, max(self.values)

    def is_one_pair(self):
        for card in self.counted:
            if self.counted[card] == 2:
                self.rest_cards.remove(card)
                return 2, card

    def is_two_pairs(self):
        pairs = []
        for card in self.counted:
            if self.counted[card] == 2:
                pairs.append(card)
        if len(pairs) == 2: 
            self.rest_cards.remove(pairs[0])
            self.rest_cards.remove(pairs[1])
            return 3, max(pairs)

    def is_three_of_a_kind(self):
        for card in self.counted:
            if self.counted[card] == 3:
                self.rest_cards.remove(card)
                return 4, card
            
    def is_straight(self):
        if len(set(self.values)) == len(self.values) and self.values[-1] - self.values[0] == len(self.values) - 1:
            return 5, max(self.values)
        
    def is_flush(self):
        if len(self.suits) == 1:
            return 6, max(self.values)
    
    def is_full_house(self):
        tree_of_kind = self.is_three_of_a_kind()
        if tree_of_kind and self.is_one_pair():
            return 7, tree_of_kind[1]
        
    def is_four_of_a_kind(self):
        for card in self.counted:
            if self.counted[card] == 4:
                self.rest_cards.remove(card)
                return 8, card
            
    def is_straight_flush(self):
        if self.is_straight() and self.is_flush():
            return 9, max(self.values)
        
    def is_royal_flush(self):
        if self.is_flush() and self.values == [10,11,12,13,14]: 
            return 10, 14
        
    def open_hand(self):
        for way in POKER:    
            self.rest_cards = set(self.values) 
            result = getattr(self, "is_" + way.lower().replace(" ", "_")) ()
            if result: return result

player1Wins = 0

for line in open("poker.txt"):
    hands = line[:-1].split(" ")
    player1, player2 = PlayerHand(hands[:5]), PlayerHand(hands[5:])
    score1, score2 = player1.open_hand(), player2.open_hand()
    if score1 == score2:
        player1Wins += 1 if max(player1.rest_cards) > max(player2.rest_cards) else 0
    else:
        player1Wins += 1 if score1 > score2 else 0
       
print ("Player 1 wins %d hands" % player1Wins)