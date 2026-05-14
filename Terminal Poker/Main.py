from Card import Card
from Deck import Deck
from Player import Player

deck = Deck()
playerCount = 2
players = []
game_state = ""
pot = 0
table = []

class Game:
    def __init__(self, playerCount=2):
        
        self.deck = Deck()
        self.playerCount = playerCount
        self.game_state = ""
        self.pot = 0
        self.table = []
        self.players = [Player() for i in range(playerCount)]
        self.active_players = self.playerCount

    def printCards(self, a):
        for i in a:
            print(i)

    def printPlayers(self, a):
        for i in a:
            self.printCards(i.hand)

    def start_round(self):
        deck.shuffle()
        self.game_state = "preflop"
        self.pot = 0
        self.active_players = self.playerCount
        for player in self.players:
            player.hand = deck.dealCards(2)
            printCards(player.hand)

        self.start_betting()

    def start_betting(self):
        
        if(self.game_state == "end"): return
        if(self.active_players == 1):
            self.game_state = "end"
            self.evaluate_winner()
            return

        prev_bet = 0
        #print(players)
        #prva runda betovanja
        for player in self.players:
            if(player.folded == True or player.allIn == True): continue
            if(self.active_players == 1):
                if(prev_bet == 0):
                    self.evaluate_winner()
                    return
                bet = player.bet(prev_bet)
                while(bet == -1): bet = player.bet(prev_bet)
                self.evaluate_winner()
                return

            bet = player.bet(prev_bet)
            while(bet == -1): bet = player.bet(prev_bet)
            if(bet > prev_bet):
                prev_bet = bet
            self.pot += bet
            print(f"NMajjac + {player.curr_bet}")
            if(player.folded == True or player.allIn == True):
                self.active_players -= 1

        i = 0
        #moraju svi da matchuju pot
        while(self.players[i].curr_bet != prev_bet):
            print(prev_bet)
            if(self.players[i].folded == True or self.players[i].allIn == True): continue
            if(self.active_players == 1):
                if(prev_bet == 0):
                    self.evaluate_winner()
                    return
                bet = self.players[i].bet(prev_bet)
                while(bet == -1): bet = self.players[i].bet(prev_bet)
                self.evaluate_winner()
                return

            bet = self.players[i].bet(prev_bet)
            while(bet == -1): bet = self.players[i].bet(prev_bet)
            if(bet > prev_bet): prev_bet = bet
            self.pot += bet
            if((self.players[i].folded == True or self.players[i].allIn == True) and self.active_players != 1):
                self.active_players -= 1
            i += 1
            i = i%self.playerCount

        if(self.active_players == 1 or self.game_state == "river"):
            self.game_state = "end"
            self.evaluate_winner()
            return
        
        if(self.game_state == "preflop"):
            self.table.extend(deck.dealCards(3))
            self.game_state = "flop"
        elif(self.game_state == "flop"):
            self.table.extend(deck.dealCards(1))
            self.game_state = "turn"
        elif(self.game_state == "turn"):
            self.table.extend(deck.dealCards(1))
            self.game_state = 'river'
        
        for i in self.table:
            print(f"{i.rank}{i.suit} ", end="")
        print(self.game_state)
        self.start_betting()


    def evaluate_winner(self):
        self.game_state = "end"
        print("Reached ENDING")
        self.table.extend(deck.dealCards(5-len(table)))


        

def main():
    game = Game()
    game.start_round()
    
def printCards(a):
    for i in a:
        print(i)

if __name__ == "__main__":
    main()