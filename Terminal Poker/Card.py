class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.dRank, self.dSuit = self.decode()

    def __str__(self):
        return self.rank + self.suit
    
    def decode(self):
        decodedRank = 0
        decodedSuit = 0
        match self.rank:
            case 'A':
                decodedRank = 14
            case 'K':
                decodedRank = 13
            case 'Q':
                decodedRank = 12
            case 'J':
                decodedRank = 11
            case _:
                decodedRank = int(self.rank)

        match self.suit:
            case '♠':
                decodedSuit = 0
            case '♥':
                decodedSuit = 1
            case '♦':
                decodedSuit = 2
            case '♣':
                decodedSuit = 3
        
        return (decodedRank, decodedSuit)