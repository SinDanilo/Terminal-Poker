from Card import Card
from Deck import Deck
from Player import Player

deck = Deck()
playerCount = 2
players = []
game_state = ""
pot = 0
table = []

def main():
    card = Card("K", "h")    
    print(card)
    start_round()
    printPlayers()
    
    while(game_state != "end"):
        for player in players:
            if(player.folded == True or player.allIn == True):
                continue
            player.bet()

        print(game_state)
        if(game_state == "preflop"):
            
            table.append(deck.dealCards(3))
            printCards(table)
            
    
def printCards(a):
    for i in a:
        print(i)

def start_round():
    deck.shuffle()
    game_state = "preflop"
    pot = 0
    for i in range(playerCount):
        players.append(Player())
        players[i].hand = list(deck.dealCards(2)) 
        players[i].chips = 1000

def printPlayers():
    for player in players:
        print(f" {player.hand[0]} {player.hand[1]}")

if __name__ == "__main__":
    main()