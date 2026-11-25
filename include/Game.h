#ifndef GAME_H
#define GAME_H

#include "include/Deck.h"
#include "include/Player.h"

#include <vector>

enum class GameState {
    Preflop,
    Flop,
    Turn,
    River,
    Showdown,
    Finished
};

class Game{
private:
    int playerCount;
    int activePlayers;
    Deck deck;
    int bigBlind = 10;
    int smallBlind = 5;
    std::vector<Player> players;
    std::vector<Card> table;
    GameState gameState;
    //Table table;
public:
    Game(int playerCount);

    void startHand();

    void startBetting();

    void evaluateWinner();
};

#endif