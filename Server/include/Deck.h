#ifndef DECK_H
#define DECK_H

#include "Card.h"
#include <algorithm>
#include <random>

class Deck {
private:
    std::vector<Card> deck;
    int counter;

public:
    Deck();

    void shuffle();
    void dealCards(int n = 1, std::vector<Card>& v);
};

#endif