#! python3

#we need to make a random choice
import random

#I want to be able to read and write from a file
import csv

#I want to write the date to a file
import datetime

cards=0
MyCards=[]

#today's date
#ThisDate=datetime.datetime.now
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
    MyCards.append(MyCard)
    notes=input("Would you like to add a note? Y/N:")
    if notes=="Y" or notes=="Yes" or notes=="yes" or notes=="y":
        MyNote=input("Enter your notes and then hit enter.")
    else:
        print("Skipping notes...") 

    
#If the user chose 3 cards / past preset future

elif int(Reading)== 3:
    print("Here are your past, present, and future cards: ")
    #while the number of cards is less than three, draw and print a new card
    if cards < 3:
       card=random.choice(MajorArcana)       
       MyCards.append(card)
       print(card)
       cards=cards+1          
    elif cards==3:
        notes=input("Would you like to add a note? Y/N:")
        if notes=="Y" or notes=="Yes" or notes=="yes" or notes=="y":
            MyNote=input("Enter your notes and then hit enter.")
        else:
            print("Skipping notes...") 
else:
    print("No cards are pulled today.")     
       
TodaysReading={
 #   "Date":ThisDate,
    "MyCards":MyCards,
    "Notes":MyNote
}
   

w = csv.writer(open( "MyReading.csv", "w"))
for key, val in TodaysReading.items():
    w.writerow([val])
print("Your reading was written to My readings.csv")
    
