CARDS = "23456789TJQKA"
CARDS_VALUES = dict(zip(CARDS, range(2,15))) # {'2':2, '3':3, ..., 'K':13, 'A':14}
POKER = ['Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight', 'Three of a Kind', 'Two Pairs', 'One Pair', 'High Card']

class PlayerHand:
    def __init__(self, cards, name):
        self.name    = name
        self.values  = sorted ( [CARDS_VALUES[i[0]] for i in cards] )   # [2,2,11,14,14]
        self.suits   = set    ( [i[1] for i in cards] )                 # {'H','C','S'}
        self.counted = self.count_cards()                               # {2:2, 11:1, 14:2}
        self.rest_cards = {}

    def count_cards(self):
        result = {}
        for val in self.values:
            result[val] = result.get(val, 0) + 1
        return result

    # -------
    def is_high_card(self):
        return 1, max(self.values)

    def is_one_pair(self):
        for card in self.counted:
            if self.counted[card] == 2:
                self.rest_cards.remove(card) # remove cards that match (leave only cards than don't make any combinations (for compare if two ranks tie))
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
    # -------
    
    def open_hand(self):
        for way in POKER:    
            self.rest_cards = set(self.values)
            result = getattr(self, "is_" + way.lower().replace(" ", "_")) () # 'Four of a Kind' -> self.is_four_of_a_kind()
            # result consists: (score, card) 
            # (4, 14) - Three of a Kind with card Ace, (3, 11) - Two Pairs with highest card Jack
            if result: 
                print ("%s: %s (with card: %s)" % (self.name, way, CARDS[result[1]-2])) 
                return result

player1Wins = 0

for i, line in enumerate(open("poker-test.txt"), 1):
    print ("#", i)
    
    hands = line[:-1].split(" ")
    player1, player2 = PlayerHand(hands[:5], "Player 1"), PlayerHand(hands[5:], "Player 2")
    score1, score2 = player1.open_hand(), player2.open_hand()
    if score1 > score2:
        print (player1.name + " Win!")
        player1Wins += 1
    elif score1 < score2:
        print (player2.name + " Win!")
    else:
        # if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared 
        print ("Two players have the same ranked hands. The highest card is", max(player1.rest_cards|player2.rest_cards))
        if max(player1.rest_cards) > max(player2.rest_cards):
            print (player1.name + " Win!")
            player1Wins += 1
        else:
            print (player2.name + " Win!")
        
print ("Player 1 wins %d hands" % player1Wins)