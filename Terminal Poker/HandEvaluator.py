from Card import Card

def isQuads(sameRank, highCard):
    ans = []
    if(len(sameRank[2]) == 1):
        ans.append(sameRank[2][0])
        ans.append(sameRank[2][0])
        ans.append(sameRank[2][0])
        ans.append(sameRank[2][0])

        i = len(highCard) - 1
        while(highCard[i] == sameRank[2][0]): i -= 1
        ans.append(highCard[i])
        ans.append(8)
        return ans
    else:
        return []


def isFullHouse(sameRank, highCard):
    ans = []
    if(len(sameRank[1]) != 0 and len(sameRank[0]) != 0):
        trips = sameRank[1][len(sameRank[1])-1]
        pairs = sameRank[0][len(sameRank[0])-1]
    elif(len(sameRank[1]) == 2):
        trips = sameRank[1][1]
        pairs = sameRank[1][0]
    else:
        return []
    
    ans.append(trips)
    ans.append(trips)
    ans.append(trips)
    ans.append(pairs)
    ans.append(pairs)
    ans.append(7)
    return ans
        
def isStraight(cards):
    ans = []
    longest = 1
    for card in cards:
        if(card == 14):cards.append(1)
    
    cards = sorted(cards, reverse=False)
    pom = -1
    #print(cards)
    for i in range(1, len(cards)):
        if(cards[i] == cards[i-1]):
            continue
        
        #print(cards[i])
        #print(cards[i-1])
        if(cards[i] == cards[i-1] + 1):
            longest += 1
            #print(longest)
        else:
            if(longest > 4):
                pom = i-1
            longest = 1
        
    if(longest > 4):
        pom = i
    if(pom != -1):
        straightFlush = True
        for i in range(5):
            ans.append(cards[pom]-i)
    return ans


def isTrips(sameRank, highCard):
    pass


def evaluateHand(cards):
    rankFreq = [0 for _ in range(15)] # number of times card is in hand
    suitFreq = [[], [], [], []]
    sameRank = [[], [], []] #pairs trips and quads
    highCard = []
    ans = []
    #vidimo koliko puta se pojavljuje isti rank i suit u ruku
    for card in cards:
        rankFreq[card.dRank] += 1
        suitFreq[card.dSuit].append(card.dRank)
        highCard.append(card.dRank)
        if(card.dRank == 14): 
            highCard.append(1)

    #ubacujemo parove tripove i quadove
    for rank, freq in enumerate(rankFreq):
        if(freq > 1):
            sameRank[freq-2].append(rank) # ako se pojavaljuje 3 puta ubaciga ga na 3-2 = 1. mjesto u nizu ( 4-2, 3-1, 2-0)
    
    #sortiramo rankove
    for rank in sameRank: rank = sorted(rank)


    highCard.sort()
    print(sameRank)
    
    #flush i straight flush
    flush = False
    straightFlush = False
    for suits in suitFreq:
        if(len(suits) > 4):
            
            cards = sorted(suits)
            ans = isStraight(cards)
            if(ans != []):
                ans.append(9)
                straightFlush = True
                print(ans)
                return ans
            
            Flush = True
            flushAns = []
            for card in cards[-5:]:
                flushAns.append(card)
            flushAns.append(6)
                
    #Quads 8
    ans = isQuads(sameRank, highCard)
    if(ans != []): return ans

    #Full House 7
    ans = isFullHouse(sameRank, highCard)
    if(ans != []): return ans

    #Flush 6
    if(flush):
        return flushAns
    
    #Straight 5
    ans = isStraight(highCard)
    if(ans != []):
        ans.append(5)
        print(ans)
        return ans

    #Three of a kind 4
    ans = isTrips(sameRank, highCard)
    print(ans)


def main():
    #['♠','♥','♦','♣']
    cards = [
        Card('A', '♠'),
        Card('10', '♣'),
        Card('5', '♠'),
        Card('4', '♠'),
        Card('3', '♠'),
        Card('2', '♠'),
        Card('8', '♦')
    ]
    evaluateHand(cards)

if __name__ == "__main__":
    main()