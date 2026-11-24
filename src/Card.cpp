#include "include/Card.h"

Card::Card(std::string rank, std::string suit){
    this->rank = rank;
    this->suit = suit;
    this->dRank = decode(rank);
    this->dSuit = decode(suit);
}

int Card::decode(std::string c){

    int decoded;

    if (c == "A") decoded = 14;
    else if (c == "K") decoded = 13;
    else if (c == "Q") decoded = 12;
    else if (c == "J") decoded = 11;
    else decoded = std::stoi(c);

    if (c == "♠") decoded = 0;
    else if (c == "♥") decoded = 1;
    else if (c == "♦") decoded = 2;
    else if (c == "♣") decoded= 3;

    return decoded;
}

void Card::printCard(){
    std::cout << rank << suit << std::endl;
}