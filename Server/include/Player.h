#ifndef PLAYER_H
#define PLAYER_H

#include <vector>
#include <string>
#include "Card.h"

class Player {
public:
    std::string name;
    int chips = 1000;

    std::vector<Card> hand;

    bool folded = false;
    bool allIn = false;

    int currentBet = 0;
    int totalContribution = 0;
    int bet(int min);
};

#endif