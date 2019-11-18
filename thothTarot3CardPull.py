#! python3
import random
import time

MajorArcana = {
    0: "The Fool ",
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

input("Let's pull some cards from the Thoth Tarot deck's Major Arcana for you. Hit Enter to begin!")
time.sleep(2)

#this is the list of cards I draw
mycards=[]
#this is a list of tarot numbers available
tarotnumbers=list(MajorArcana)
#this will choose a number/card from tarot number and then remove it from the deck and add it to my cards
card1=random.choice(tarotnumbers)
tarotnumbers.remove(card1)
mycards.append(card1)

#the prior, draw, remove from deck, add to my cards is performed again
card2=random.choice(tarotnumbers)
tarotnumbers.remove(card2)
mycards.append(card2)

#the prior, draw, remove from deck, add to my cards is performed again
card3=random.choice(tarotnumbers)
tarotnumbers.remove(card3)
mycards.append(card3)

#To select the value assoaciated with each key-value pair
print("**Shuffling**")
time.sleep(2)

print("Your first card is "+MajorArcana.get(card1)+".")
time.sleep(2)

print("Your second card is "+MajorArcana.get(card2)+".")
time.sleep(2)

print("Your third card is "+MajorArcana.get(card3)+".")
time.sleep(2)

print("Thanks for playing.")
time.sleep(2)

#alternatively this can be printed as :
#myspread=[MajorArcana.get(card1),MajorArcana.get(card2),MajorArcana.get(card3)]
#print(myspread)

		
