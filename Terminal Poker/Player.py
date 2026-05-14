class Player:
    def __init__(self):
        self.hand = []
        self.chips = 0
        self.name = ""
        self.folded = False
        self.allIn = False

    def bet(self):
        s = input()

        #clean up ovo kasnije zbog retarda koji budu igrali ovo
        if(s == "Fold"):
            self.folded = True
            return 0
        elif(s == "All In"):
            a = self.chips
            self.chips = 0
            self.allIn = True
            return a
        else:
            s = int(s)
            self.chips -= s
            return s
            


    
