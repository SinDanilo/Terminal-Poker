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
        for i in [4, 3, 2, 1, 0]:
            ans.append(cards[pom]-i)
    return ans

def isTrips(sameRank, highCard):
    ans = []
    if(len(sameRank[1]) != 0):
        trips = sameRank[1][len(sameRank[1])-1]
        ans.append(trips)
        ans.append(trips)
        ans.append(trips)

        i = len(highCard) - 1
        while(len(ans) != 5):
            while(highCard[i] == trips):
                i -= 1
            ans.append(highCard[i])
            i -= 1
        ans[3], ans[4] = ans[4], ans[3]
        ans.append(4)
        return ans
    else:
        return []

def isTwoPair(sameRank, highCard):
    ans = []
    if(len(sameRank[0]) >= 2):
        l = len(sameRank[0])-1
        pair1 = sameRank[0][l]
        pair2 = sameRank[0][l-1]
        ans.append(pair1)
        ans.append(pair1)
        ans.append(pair2)
        ans.append(pair2)
        i = len(highCard) - 1
        while(highCard[i] == pair1 or highCard[i] == pair2): i -= 1
        ans.append(highCard[i])
        ans.append(3)
        return ans
    else:
        return []

def isPair(sameRank, highCard):
    ans = []
    if(len(sameRank[0]) != 0):
        ans.append(sameRank[0][0])
        ans.append(sameRank[0][0])
        i = len(highCard) - 1
        while(len(ans) != 5):
            while(highCard[i] == sameRank[0][0]):
                i -= 1
            ans.append(highCard[i])
            i -= 1
        ans[2], ans[3], ans[4] = ans[4], ans[3], ans[2]
        ans.append(2)
        return ans
    else:
        return []

def isHighCard(highCard):
    ans = []
    i = len(highCard) - 1
    while(len(ans) != 5):
        ans.append(highCard[i])
        i -= 1
    ans.sort()
    ans.append(1)
    return ans

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
    #print(sameRank)
    #print(highCard)
    #print(suitFreq)
    #flush i straight flush 9
    flush = False
    straightFlush = False
    for suits in suitFreq:
        if(len(suits) > 4):
            
            for card in suits:
                if(card == 14):suits.append(1)

            cards = sorted(suits)
            #print(cards)
            ans = isStraight(cards)
            if(ans != []):
                ans.append(9)
                straightFlush = True
                print(ans)
                return ans
            
            flush = True
            flushAns = []
            for card in cards[-5:]:
                flushAns.append(card)
            flushAns.append(6)
                
    #Quads 8
    ans = isQuads(sameRank, highCard)
    #print(ans)
    if(ans != []): return ans

    #Full House 7
    ans = isFullHouse(sameRank, highCard)
    #print(ans)
    if(ans != []): return ans

    #Flush 6
    if(flush):
        #print(flushAns)
        return flushAns
    
    #Straight 5
    ans = isStraight(highCard)
    if(ans != []):
        ans.append(5)
        print(ans)
        return ans

    #Three of a kind 4
    ans = isTrips(sameRank, highCard)
    #print(ans)
    if(ans != []): return ans

    #Two pair 3
    ans = isTwoPair(sameRank, highCard)
    #print(ans)
    if(ans != []): return ans

    #Pair 2
    ans = isPair(sameRank, highCard)
    #print(ans)
    if(ans != []): return ans

    ans = isHighCard(highCard)
    #print(ans)
    return ans

def evaluateWinner(hand1, hand2):
    if(hand1[5] > hand2[5]):
        return 1
    elif(hand1[5] < hand2[5]):
        return -1
    
    #sada ako imaju isti rank ruke
    id = hand1[5]
    #straigh flush i straight
    if(id == 9 or id == 5):
        if(hand1[4] > hand2[4]):
            return 1
        elif(hand1[4] < hand2[4]):
            return -1
        else:
            return 0
    #Quads
    if(id == 8):
        if(hand1 == hand2):return 0

        if(hand1[0] > hand2[0]):
            return 1
        elif(hand1[0] < hand2[0]):
            return -1
        elif(hand1[4] > hand2[4]):
            return 1
        else:
            return -1

    #Full House
    if(id == 7):
        if(hand1 == hand2):return 0

        if(hand1[0] > hand2[0]):
            return 1
        elif(hand1[0] < hand2[0]):
            return -1
        elif(hand1[4] > hand2[4]):
            return 1
        else:
            return -1

    #Flush
    if(id == 6):
        i = 4
        if(hand1 == hand2): return 0

        while(hand1[i] == hand2[i]):
            i -= 1
        if(hand1[i] > hand2[i]):
            return 1
        else:
            return -1

    #Three of a kind
    if(id == 4):
        if(hand1 == hand2):return 0
        if(hand1[0] > hand2[0]):
            return 1
        elif(hand1[0] < hand2[0]):
            return -1
        elif(hand1[3] > hand2[3]):
            return 1
        elif(hand1[3] < hand2[3]):
            return -1
        elif(hand1[4] > hand2[4]):
            return 1
        elif(hand1[4] < hand2[4]):
            return -1

    #Two pair
    if(id == 3):
        if(hand1 == hand2):return 0
        if(hand1[0] > hand2[0]):
            return 1
        elif(hand1[0] < hand2[0]):
            return -1
        elif(hand1[2] > hand2[2]):
            return 1
        elif(hand1[2] < hand2[2]):
            return -1
        elif(hand1[4] > hand2[4]):
            return 1
        elif(hand1[4] < hand2[4]):
            return -1

    #Pair
    if(id == 2):
        if(hand1 == hand2):return 0
        if(hand1[0] > hand2[0]):
            return 1
        elif(hand1[0] < hand2[0]):
            return -1
        else:
            i = 4
            while(hand1[i] == hand2[i]):
                i -= 1
            if(hand1[i] > hand2[i]):
                return 1
            else:
                return -1

    if(id == 1):
        if(hand1 == hand2): return 0
        i = 4
        while(hand1[i] == hand2[i]):
            i -= 1
        if(hand1[i] > hand2[i]):
            return 1
        else:
            return -1


def main():
    #['♠','♥','♦','♣']
    cards = [
        Card('10', '♥'),
        Card('A', '♣'),
        Card('5', '♥'),
        Card('4', '♥'),
        Card('2', '♣'),
        Card('9', '♥'),
        Card('7', '♣')
    ]
    evaluateHand(cards)
    print(evaluateWinner([1,11,12,13,5,1], [9,10,12,13,4 ,1]))

if __name__ == "__main__":
    main()