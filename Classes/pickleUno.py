# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 19:11:13 2021

@author: Aadhavan
"""
import random

import pickle
#print("o")
class UnoCardManager:
    stackOfCards = []
    players = []
    def addCard(self,unoCard):
        self.stackOfCards.append(unoCard)
       # print(unoCard)
        
    def removeCard(self,unocard):
        self.stackOfCards.remove(unocard)
        
    def addPlayer(self,player1):
        self.players.append(player1)
    def Print(self):
        for p in self.players:
            p.Print()
        for s in self.stackOfCards:
            s.Print()
        pass;
        
    def validateCards(self, unoCard1, unoCard2):
        status = False
        if(unoCard1.power == True):
            status = self.validatePowerCard(unoCard1, unoCard2)
        else:
            status = self.validateRegularCard(unoCard1, unoCard2)
        unoCard1.Print()
        unoCard2.Print()

        print(status)

    def validateRegularCard(self, unoCard1, unoCard2):
        if (not unoCard2.power):
            if unoCard1.color == unoCard2.color or unoCard1.value == unoCard2.value:
                return True
            else:
                return False
        else:
            #wild card and +4 card  are power cards
            #TODO
            return True
        
    def validatePowerCard(self, unoCard1, unoCard2):
        if (unoCard1.value == "wild"):
            return self.validateWildCard(unoCard1,unoCard2)
        if (unoCard1.value == "+4"):
            return self.validatePlus4Card(unoCard1,unoCard2)
        
        return True
        
    def validateWildCard(self, unoCard1, unoCard2):
        if unoCard1.color == unoCard2.color:
            return True
        else: 
            if  unoCard1.power == unoCard2.power:
                return True
            else:
                return False
            
    def validatePlus4Card(self, unoCard1, unoCard2):
        if unoCard1.color == unoCard2.color:
            print("1")
            return True
        else: 
            if  unoCard1.power == unoCard2.power:
                return True
            else:
                return False
            
    def random_cards(self, no_of_cards):     
        
        index = 1
        randCards = []
        while (index <= no_of_cards):
            cards = len(self.stackOfCards)-1
            randNumber = random.randint(0,cards)
            index += 1
            print(index)
            randCards.append(self.stackOfCards[randNumber])
            self.stackOfCards.remove(self.stackOfCards[randNumber])
        
        return randCards
            
            
    # TODO now - it has to return any no_of_cards random cards as a list
    


       
            
    def validateCards_old(self,Card1,Card2):
        index = 0
        if Card1.color == Card2.color or Card2.color == "":
            index += 1
        if Card1.value == Card2.value:
            index += 1
        
        if Card2.power:
            if Card1.value != "+2" or Card1.value != "skip":
                index += 0
            else:
                index += 1
                
        if index >= 1:
            print("correct")
        else: 
            print("wrong")
            
class  Player:   
    playerCards = []
    def __init__(self,name):
        self.name = name
        
    def add(self, unoCard):
        self.playerCards.append(unoCard)
        
    def Print(self):
        print("This player's name is", self.name)
        for c in self.playerCards:
            c.Print()
        pass;

    

class UnoCard:
    
    def __init__ (self, color, value, name, power, ApproprioteUse):
        self.color = color
        self.value = value
        self.name = name
        self.power = power
        self.ApproprioteUse = ApproprioteUse
    
    def Print (self):
        print("The card color is", self.color, ", value is", self.value,", is called" , 
              self.name, ", power =", self.power)
        #print("You can use this card" , self.ApproprioteUse)
#        if self.isPowerCard() == True:
#            print("This is a power card.")
#        else:
#            print("This is not a power card.")
        
    def isPowerCard(self):
        if self.power == True:
            return True
        else:
            return False

        
                      
                      
red5Card = UnoCard("red", 5, "red 5", False, "when color is red or 5")
blue7Card = UnoCard("blue", 5, "blue 7", False, "when color is blue or 7")
yellowPlus2Card = UnoCard("yellow", "+2", "Yellow+2", False, "when color is yellow or card is +2")
greenSkipCard = UnoCard("green", "skip", "green Skip", False,"when color is green or card is skip")
plusFourRed = UnoCard("red", "+4", "+4", True, "anytime unless player is skipped or forced to take some cards")
greenPlus2Card = UnoCard("green", "+2", "green+2", False, "when color is green or card is +2")
plusFourGreen = UnoCard("green", "+4", "+4", True, "anytime unless player is skipped or forced to take some cards")

wildRedCard = UnoCard("red", "wild", "wild", True, "anytime unless player is skipped or forced to take some cards")
wildBlueCard = UnoCard("blue", "wild", "wild", True, "anytime unless player is skipped or forced to take some cards")

##red5Card.Print()
manager = UnoCardManager()

manager.addCard(red5Card)
manager.addCard(blue7Card)
manager.addCard(greenSkipCard)
print ("printing cards")
cards =manager.random_cards(3)
for card in cards:
    card.Print()
manager.validateCards(wildRedCard,blue7Card)  #correct
#manager.validateCards(red5Card,blue7Card)  #correct
#manager.validateCards(red5Card,yellowPlus2Card)  #wrong
##manager.validateCards(plusFourRed,green+2Card)  #wrong
#manager.validateCards(greenPlus2Card,plusFourRed)  #wrong - fail
#manager.validateCards(greenSkipCard,plusFourRed)  #correct
#manager.validateCards(yellowPlus2Card,blue7Card)  #wrong
##manager.validateCards(plusFourRed,plusFourRed)  #correct
#manager.validateCards(blue7Card,greenPlus2Card)  #wrong
#manager.validateCards(red5Card,plusFourRed)  #correct
##manager.validateCards(plusFourGreen,plusFourRed)  #correct
#manager.validateCards(wildRedCard,plusFourRed)  #correct
#manager.validateCards(wildRedCard,plusFourGreen)  #correct
#manager.validateCards(plusFourGreen, plusFourRed)
#manager.validateCards(plusFourGreen, greenPlus2Card)
#manager.validateCards(plusFourGreen, blue7Card)
#manager.validateCards(blue7Card, plusFourGreen)
#manager.validateCards(wildRedCard, plusFourGreen)
#manager.validateCards(plusFourGreen, wildRedCard)


#manager.addCard(Card1)
#
#player = Player("Oscar")
##player.add(Card2)
##player.add(plusFourRed)
#manager.addPlayer(player)
#manager.Print()

#player.Print()
#storage = open("Storage.txt","wb")
#
#pickle.dump(red5Card,storage)
#pickle.dump(Card2,storage)
#pickle.dump(yellow+2Card,storage)
#pickle.dump(greenSkipCard,storage)
#pickle.dump(plusFourRed,storage)
#storage.close()
# 
#load_file = open('storage.txt',"rb")
#card_data = pickle.load(load_file)
#card_data.Print()
#card_data = pickle.load(load_file)
#card_data.Print()
#card_data = pickle.load(load_file)
#card_data.Print()
#card_data = pickle.load(load_file)
#card_data.Print()
#card_data = pickle.load(load_file)
#card_data.Print()
#
#load_file.close()        new = []
      
#  cards = len(self.stackOfCards)-1
#        index = 0
#        while index <= no_of_cards:
#            randnumber = random.randint(0,cards)
#            index += 1
#            print(index)
#            randCard = self.stackOfCards[randnumber]
#            new.append(randCard)
#            self.removeCard(self.stackOfCards[randnumber])