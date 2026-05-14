from Card import Card
import random

class Deck:
    def __init__(self):
        self.deck = [Card(rank, suit) for rank in ('2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K", "A")
                     for suit in ['♠','♥','♦','♣']]
        self.counter = 0


    def shuffle(self):
        
        random.shuffle(self.deck)
        self.counter = 0

    def dealCards(self, n = 1):
        hand = []
        for num in range(n):
            hand.append(self.deck[self.counter])
            self.counter += 1
        return list(hand)
