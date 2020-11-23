#BlackJack

import random
#Create a Deck
class deck():
    def __init__(self):
        self.Deck = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":11}
        
    def shuffle(self):
        return random.choice(list(self.Deck.keys()))
    
 
    

    
class BlackJack(deck):
    def __init__(self):
        super().__init__()
        self.__dealer = []
        self.player = []
        self.start()
        
    def start(self):
        for i in range(2):
            self.__dealer.append(self.shuffle())
            self.player.append(self.shuffle())
            
        self.showhands()
        self.begin()
        
     
    def begin(self):
        if self.CheckSum(self.player) >= 21:
            self.showhands()
            print("Player Busted !")
            return
        
        print("Hit or Stay ?")
        x = input().lower()
        
        if x == "hit":
            self.player.append(self.shuffle())
            self.showhands()
            self.begin()        
        else:
            self.dealerturn()
            
           
    def dealerturn(self):
        print("Dealer's turn")
        pass
    
    def CheckSum(self,deck):
        sum = 0
        for i in deck:
            sum+=self.Deck[i]
        return sum

        
    def showhands(self):
        print(self.__dealer[:-1])
        print(self.player)    
        
    
game= BlackJack()


        
        
        
        
        
        
    