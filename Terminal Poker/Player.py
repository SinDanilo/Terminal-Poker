class Player:
    def __init__(self):
        self.hand = []
        self.chips = 1000
        self.name = ""
        self.folded = False
        self.allIn = False
        self.curr_bet = 0

    def bet(self, prev_bet):
        #print("OKJ")
        s = input("1) Fold  2) Call  3) Raise \n")
        s = s.lower().strip()
        #clean up ovo kasnije zbog retarda koji budu igrali ovo
        if(s == "fold" or s == "1"):
            self.folded = True
            self.curr_bet = 0
            return 0
        elif(s == "call" or s == "2"):
            a = self.chips
            self.curr_bet = prev_bet
            if(a < prev_bet):
                self.allIn = True
                self.curr_bet = a
                self.chips = 0
            if(self.chips != 0): self.chips -= self.curr_bet
            return self.curr_bet
        elif(s == "3" or s.isnumeric()):
            if(s == "3"):
                s = input("Bet size: ")
                
            if(not s.isnumeric() or int(s) < prev_bet):
                    print("Incorrect input")
                    return -1

            a = int(s)
            self.curr_bet = a
            if(a > self.chips):
                a = self.chips
                self.chips = 0
                self.curr_bet = a
                self.allIn = True
                return a
            else:
                self.chips -= a
                return a
        else:
            print("Incorrect input")
            return -1
            
            


    
