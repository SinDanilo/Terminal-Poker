#include "include/Deck.h"


Deck::Deck() : counter(0) {
    std::vector<std::string> ranks = {
        "2", "3", "4", "5", "6", "7",
        "8", "9", "10", "J", "Q", "K", "A"
    };

    std::vector<std::string> suits = {
        "♠", "♥", "♦", "♣"
    };

    for (const auto& rank : ranks) {
        for (const auto& suit : suits) {
            deck.emplace_back(rank, suit);
        }
    }
}

void Deck::shuffle() {
    static std::random_device rd;
    static std::mt19937 gen(rd());

    std::shuffle(deck.begin(), deck.end(), gen);
    counter = 0;
}

void Deck::dealCards(int n, std::vector<Card>& v) {
    std::vector<Card> hand;

    for (int i = 0; i < n; i++) {
        if (counter >= deck.size())
            break;

        hand.push_back(deck[counter]);
        counter++;
    }
    v.insert(v.end(), hand.begin(), hand.end());
    return;
}

