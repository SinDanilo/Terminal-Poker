#include "Server/include/Game.h"

Game::Game(int playerCount){
    this->playerCount = playerCount;
    this->activePlayers = playerCount;
    this->dealerPos = -1;
    this->deck = Deck();
    for(int i = 0; i < playerCount; i++){
        this->players.emplace_back();
    }
}



void Game::startHand(){
    this->gameState = GameState::Preflop;
    this->activePlayers = this->playerCount;
    this->dealerPos = (this->dealerPos + 1) % (this->playerCount);
    this->deck.shuffle();
    //brise pa deluje sve ruke
    this->table.clear();
    for(Player p : players){
        p.hand.clear();
        deck.dealCards(2, p.hand);
        p.currentBet = 0;
        p.folded = false;
        p.allIn = false;
        p.totalContribution = 0;
    }

    startBetting();
}

void Game::startBetting(){
    int curr_bet = (gameState == GameState::Preflop) ? this->bigBlind : 0;
    bool raised = true;
    bool firstRound = true;
    /*
    for(Player& p: players){
        if(p.folded || p.allIn)continue;


        if(this->activePlayers == 1){
            if(p.currentBet != curr_bet){
                int bet = p.bet(curr_bet - p.currentBet);
            }
            evaluateWinner();
            return;
        }
        int bet = p.bet(curr_bet - p.currentBet);
        if(p.folded || p.allIn){
            this->activePlayers--;
            continue; //foldovao je player
        } 
        p.currentBet += bet;
        if(p.currentBet > curr_bet){
            curr_bet = p.currentBet;
            raised = true;
        }
    }
*/
    while(raised){
        raised = false;

        //for(int i = (this->dealerPos + 2)%(this->playerCount); i !=)


        for(Player& p: players){
            if(p.folded || p.allIn)continue;

            if((p.currentBet == curr_bet) && !firstRound){
                break;
            }
            if(this->activePlayers == 1){
                if(p.currentBet != curr_bet){
                    int bet = p.bet(curr_bet - p.currentBet);
                }
                evaluateWinner();
                return;
            }
            int bet = p.bet(curr_bet - p.currentBet);
            
            if(p.folded || p.allIn){
                this->activePlayers--;
                continue; //foldovao je player
            }
            
            if(p.currentBet > curr_bet){
                curr_bet = p.currentBet;
                raised = true;
            }

        }
        firstRound = false;
    }

    for(Player& p : players) p.currentBet = 0;

    if(this->gameState == GameState::Preflop){
        this->deck.dealCards(3, table);
        this->gameState = GameState::Flop;
    }else if(gameState == GameState::Flop){
        this->deck.dealCards(1, table);
        this->gameState = GameState::Turn;
    }else if(gameState == GameState::Turn){
        this->deck.dealCards(1, table);
        this->gameState = GameState::River;
    }else if(gameState == GameState::River){
        evaluateWinner();
    }
    startBetting();
}