#include "Server/include/EvaluateWinner.h"

#include <algorithm>
#include <array>

namespace {

using Hand = std::vector<int>;
using SameRank = std::array<std::vector<int>, 3>;

// 8 - Four of a kind
Hand isQuads(const SameRank& sameRank, const Hand& highCard) {
    Hand ans;

    if (sameRank[2].empty())
        return ans;

    int quad = sameRank[2].back();

    for (int i = 0; i < 4; i++)
        ans.push_back(quad);

    for (int i = static_cast<int>(highCard.size()) - 1; i >= 0; i--) {
        if (highCard[i] != quad && highCard[i] != 1) {
            ans.push_back(highCard[i]);
            break;
        }
    }

    ans.push_back(8);
    return ans;
}

// 7 - Full house
Hand isFullHouse(const SameRank& sameRank) {
    Hand ans;

    int trips = -1;
    int pair = -1;

    if (!sameRank[1].empty()) {
        trips = sameRank[1].back();

        if (!sameRank[0].empty()) {
            pair = sameRank[0].back();
        }
        else if (sameRank[1].size() >= 2) {
            pair = sameRank[1][sameRank[1].size() - 2];
        }
    }

    if (trips == -1 || pair == -1)
        return ans;

    ans.insert(ans.end(), 3, trips);
    ans.insert(ans.end(), 2, pair);
    ans.push_back(7);

    return ans;
}

// 5 - Straight
Hand isStraight(Hand cards) {
    Hand ans;

    std::sort(cards.begin(), cards.end());
    cards.erase(std::unique(cards.begin(), cards.end()), cards.end());

    // Ace can also be used as rank 1 for A-2-3-4-5.
    if (!cards.empty() && cards.back() == 14)
        cards.insert(cards.begin(), 1);

    int longest = 1;
    int highestStraight = -1;

    for (int i = 1; i < static_cast<int>(cards.size()); i++) {
        if (cards[i] == cards[i - 1] + 1) {
            longest++;
        }
        else {
            longest = 1;
        }

        if (longest >= 5)
            highestStraight = cards[i];
    }

    if (highestStraight == -1)
        return ans;

    for (int i = highestStraight - 4; i <= highestStraight; i++)
        ans.push_back(i);

    return ans;
}

// 4 - Three of a kind
Hand isTrips(const SameRank& sameRank, const Hand& highCard) {
    Hand ans;

    if (sameRank[1].empty())
        return ans;

    int trips = sameRank[1].back();

    ans.insert(ans.end(), 3, trips);

    for (int i = static_cast<int>(highCard.size()) - 1;
         i >= 0 && ans.size() < 5; i--) {

        if (highCard[i] != trips && highCard[i] != 1)
            ans.push_back(highCard[i]);
    }

    if (ans.size() != 5)
        return {};

    std::sort(ans.begin() + 3, ans.end());

    ans.push_back(4);
    return ans;
}

// 3 - Two pair
Hand isTwoPair(const SameRank& sameRank, const Hand& highCard) {
    Hand ans;

    if (sameRank[0].size() < 2)
        return ans;

    int pair1 = sameRank[0].back();
    int pair2 = sameRank[0][sameRank[0].size() - 2];

    ans.insert(ans.end(), 2, pair1);
    ans.insert(ans.end(), 2, pair2);

    for (int i = static_cast<int>(highCard.size()) - 1; i >= 0; i--) {
        if (highCard[i] != pair1 &&
            highCard[i] != pair2 &&
            highCard[i] != 1) {

            ans.push_back(highCard[i]);
            break;
        }
    }

    ans.push_back(3);
    return ans;
}

// 2 - Pair
Hand isPair(const SameRank& sameRank, const Hand& highCard) {
    Hand ans;

    if (sameRank[0].empty())
        return ans;

    int pair = sameRank[0].back();

    ans.insert(ans.end(), 2, pair);

    for (int i = static_cast<int>(highCard.size()) - 1;
         i >= 0 && ans.size() < 5; i--) {

        if (highCard[i] != pair && highCard[i] != 1)
            ans.push_back(highCard[i]);
    }

    if (ans.size() != 5)
        return {};

    std::sort(ans.begin() + 2, ans.end());

    ans.push_back(2);
    return ans;
}

// 1 - High card
Hand isHighCard(const Hand& highCard) {
    Hand ans;

    for (int i = static_cast<int>(highCard.size()) - 1;
         i >= 0 && ans.size() < 5; i--) {

        if (highCard[i] != 1)
            ans.push_back(highCard[i]);
    }

    std::sort(ans.begin(), ans.end());
    ans.push_back(1);

    return ans;
}

}


//vraca najbolju ruku 
Hand HandEvaluator::evaluateHand(const std::vector<Card>& cards) {
    std::array<int, 15> rankFreq{};
    std::array<Hand, 4> suitFreq;

    SameRank sameRank;
    Hand highCard;

    // Count ranks and suits.
    for (const Card& card : cards) {
        rankFreq[card.dRank]++;
        suitFreq[card.dSuit].push_back(card.dRank);

        highCard.push_back(card.dRank);

        if (card.dRank == 14)
            highCard.push_back(1);
    }

    // Group ranks into pairs, trips and quads.
    for (int rank = 2; rank <= 14; rank++) {
        int freq = rankFreq[rank];

        if (freq >= 2 && freq <= 4)
            sameRank[freq - 2].push_back(rank);
    }

    std::sort(highCard.begin(), highCard.end());

    // 9 - Straight flush
    // 6 - Flush
    bool flush = false;
    Hand flushAns;

    for (const Hand& suit : suitFreq) {
        if (suit.size() < 5)
            continue;

        Hand suitedCards = suit;

        Hand straightCards = suitedCards;

        if (std::find(straightCards.begin(), straightCards.end(), 14)
            != straightCards.end()) {
            straightCards.push_back(1);
        }

        Hand straightFlush = isStraight(straightCards);

        if (!straightFlush.empty()) {
            straightFlush.push_back(9);
            return straightFlush;
        }

        flush = true;

        std::sort(suitedCards.begin(), suitedCards.end());

        flushAns.assign(suitedCards.end() - 5, suitedCards.end());
        flushAns.push_back(6);
    }

    // 8 - Four of a kind
    Hand ans = isQuads(sameRank, highCard);
    if (!ans.empty())
        return ans;

    // 7 - Full house
    ans = isFullHouse(sameRank);
    if (!ans.empty())
        return ans;

    // 6 - Flush
    if (flush)
        return flushAns;

    // 5 - Straight
    ans = isStraight(highCard);
    if (!ans.empty()) {
        ans.push_back(5);
        return ans;
    }

    // 4 - Three of a kind
    ans = isTrips(sameRank, highCard);
    if (!ans.empty())
        return ans;

    // 3 - Two pair
    ans = isTwoPair(sameRank, highCard);
    if (!ans.empty())
        return ans;

    // 2 - Pair
    ans = isPair(sameRank, highCard);
    if (!ans.empty())
        return ans;

    // 1 - High card
    return isHighCard(highCard);
}


int HandEvaluator::betterHand(const std::vector<int>& hand1, const std::vector<int>& hand2) {
    if (hand1[5] > hand2[5])
        return 1;

    if (hand1[5] < hand2[5])
        return -1;

    // Both hands have the same category.
    // Compare their five ranks lexicographically.
    for (int i = 0; i < 5; i++) {
        if (hand1[i] > hand2[i])
            return 1;

        if (hand1[i] < hand2[i])
            return -1;
    }

    return 0;
}

int HandEvaluator::isWinner(std::vector<Hand>& playerHands, Hand& hand, int except, std::vector<int>& winners){
    for(int i = 0; i < playerHands.size(); i++){
        if(i == except) continue; //ne poredi sam sa sobom
        int k = betterHand(hand, playerHands[i]);
        if(k == -1){
            //nije najbolja ruka
            winners.clear();
            return -1;
        }else if(k == 0){
            //Draw logika
            int pos = hand[5];
            if(winners.empty())winners.push_back(except);
            winners.push_back(i);
        }
    }
    if(!winners.empty()){
        for(int i = 0; i < winners.size(); i++){
            playerHands[winners[i]][5] = -1;
        }
        return 0;
    }
    playerHands[except][5] = -1;
    return 1;
}

void HandEvaluator::splitPot(std::vector<Player>& players, int playerPos, int pot, int splitType, std::vector<int>& winners){
    if(splitType == 1){
        //za slucaj da je pobjedio
        int winnings = 0;
        int split = players[playerPos].totalContribution;
        for(int i = 0; i < players.size(); i++){
            int loses = std::min(split, players[i].totalContribution);
            winnings += loses;
            players[i].totalContribution -= loses;
        }

        players[playerPos].chips += winnings;
        return;
    }
    // za DRAWS BOG MI POMOGAO
    // SHIT Zamjena za pravilan kod
    for(int i = 0; i < winners.size(); i++){
        players[winners[i]].chips += pot/winners.size();
    }
    return;
    
}


void HandEvaluator::evaluateWinner(std::vector<Player>& players, std::vector<Card>& table, int pot){
//extendaj table na 5 karata
//napravi unos za evaaluateHand tj  table + p.hand
//imamo vektor najboljih ruka svih igraca
//ubacimo taj vektor u isWinner fju
//snadjemo se nekako za side pots i draws
    std::vector<Hand> playerHands;
    std::vector<int> winners;
    for(Player& p : players){
        std::vector<Card> cards = p.hand;
        for(Card& c: table)cards.push_back(c);
        Hand hand = evaluateHand(cards);
        if(p.folded) hand[5] = -1;
        playerHands.push_back(hand);
    }

    for(int i = 0; i < playerHands.size(); i++){
        int k = isWinner(playerHands, playerHands[i], i, winners);
        if(k != -1){
            splitPot(players, i, pot, k, winners);
            winners.clear();
        }
    }
}
