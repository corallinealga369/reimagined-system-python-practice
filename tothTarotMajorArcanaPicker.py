#! python3

#we need to make a random choice
import random

#This is a dictionary of all the major arcana in the Thoth Tarot
MajorArcana = {
    0: "The Fool",
    1: "The Magus",
    2: "The Priestess",
    3: "The Empress",
    4: "The Emperor",
    5: "The Hierophant",
    6: "The Lovers",
    7: "The Chariot",
    8: "Adjustment",
    9: "The Hermit",
    10: "Fortune",
    11: "Lust",
    12:"The Hanged Man",
    13:"Death",
    14:"Art",
    15:"The Devil",
    16:"The Tower",
    17:"The Star",
    18:"The Moon",
    19:"The Sun",
    20:"The Aeon"
}

#prompt the user for input
print("Let's pull some cards from the Thoth Tarot desk for you. ")
Reading=input("Enter 1 to draw a daily card, enter 3 to do a past present future reading: ")

#if the user chose 1 card draw one card and print it
if int(Reading) == 1:
    MyCard=random.choice(MajorArcana)
    print(MyCard)
#If the user chose 3 cards / past preset future
elif int(Reading)== 3:
    print("Here are your past, present, and future cards: ")
    cards=0
    MyCards=[]

#while the number of cards is less than three, draw and print a new card
    while cards < 3:
       card=random.choice(MajorArcana)       
       MyCards.append(card)
       print(card)
       cards=cards+1
          
else:
    print("Please enter 1 or 3.")        

