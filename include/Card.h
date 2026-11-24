#ifndef CARD_H
#define CARD_H

#include <string>
#include <iostream>

class Card{
public:
    std::string rank, suit;
    int dRank, dSuit;
    Card(std::string rank, std::string suit);
    void printCard();
private:
    int decode(std::string c);
};

#endif