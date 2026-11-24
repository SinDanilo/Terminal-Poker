#include "include/Game.h"

Game::Game(int playerCount){
    this->playerCount = playerCount;
    this->activePlayers = playerCount;
    this->deck = Deck();
    for(int i = 0; i < playerCount; i++){
        this->players.emplace_back();
    }
}

// Append b to the end of a
//a.insert(a.end(), b.begin(), b.end());

void Game::startHand(){
    gameState = GameState::Preflop;
    this->activePlayers = playerCount;
    deck.shuffle();
    //brise pa deluje sve ruke
    table.clear();
    for(Player p : players){
        p.hand.clear();
        p.hand = deck.dealCards(2);
        p.currentBet = 0;
        p.folded = false;
        p.allIn = false;
        p.totalContribution = 0;
    }

    startBetting();
}

void Game::startBetting(){
    int curr_bet = (gameState == GameState::Preflop) ? bigBlind : 0;
    bool raised = false;
    for(Player p: players){
        if(p.folded || p.allIn)continue;
        int bet = p.bet(curr_bet - p.currentBet);
        if(bet == -1) continue; //foldovao je player
        p.currentBet += bet;
        if(bet > curr_bet){
            curr_bet = bet;
            raised = true;
        }
    }

    while(raised){
        raised = false;
        for(Player p: players){
            if(p.folded || p.allIn)continue;
            int bet = p.bet(curr_bet - p.currentBet);
            if(bet > curr_bet){
                curr_bet = bet;
                raised = true;
            }
            if(p.currentBet == curr_bet){
                break;
            }
        }
    }
    if(gameState == GameState::Preflop){
        table = deck.dealCards(3);
        gameState = GameState::Flop;
    }else if(gameState == GameState::Flop){
        //table.push_back()
    }else if(gameState == GameState::Turn){

    }else if(gameState == GameState::River){

    }
}