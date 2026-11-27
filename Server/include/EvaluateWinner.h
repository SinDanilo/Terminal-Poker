#pragma once

#include <vector>
#include "Card.h"
#include "Player.h"


class HandEvaluator {
public:

    std::vector<int> evaluateHand(const std::vector<Card>& cards);

    int betterHand(const std::vector<int>& hand1, const std::vector<int>& hand2);

    void evaluateWinner(std::vector<Player>& players, std::vector<Card>& table, int pot);

    int isWinner(std::vector<std::vector<int>>& playerHands, std::vector<int>& hand, int except, std::vector<int>& winners);

    void splitPot(std::vector<Player>& players, int playerPos, int pot, int splitType, std::vector<int>& winners);
};
