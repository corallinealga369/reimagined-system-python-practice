#! python3

import random
import string

print("Welcome to Charlie's password generator.")
print("\n")
Length=input("How long should your password be? Please enter a value 10-20 : ")
Capital=input("Should it have capital letters? Y/N ")
Lower=input("Should it have lowercase letters? Y/N ")
Numbers=input("Should it include numbers? Y/N ")
Total=input("How many passwords should be generated? Choose a number between 0 and 20.: ")
print("\n")
print("Thinking...")

if Capital=="Y" or Capital=="y":
   HasCapital=True
else: 
   HasCapital=False 
if Lower=="Y" or Lower=="y":
   HasLower=True
else: 
   HasLower=False 
if Numbers=="Y" or Numbers=="y":
   HasNumbers=True
else: 
   HasNumbers=False    
Length=int(Length)
Total=int(Total)

def randompassword(Length):
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for x in range(0,Length))
def randomalphapassword(Length):
    chars=string.ascii_uppercase + string.ascii_lowercase 
    return ''.join(random.choice(chars) for x in range(0,Length))
def randomcapitalpassword(Length):
    chars=string.ascii_uppercase 
    return ''.join(random.choice(chars) for x in range(0,Length))
def randomlowerpassword(Length):
    chars=string.ascii_lowercase 
    return ''.join(random.choice(chars) for x in range(0,Length))
def randomnumericpassword(Length):
    chars=string.digits 
    return ''.join(random.choice(chars) for x in range(0,Length))
def randomnumericlowerpassword(Length):
    chars=string.digits + string.ascii_lowercase
    return ''.join(random.choice(chars) for x in range(0,Length))
def randomcapitalnumberspassword(Length):
    chars=string.digits + string.ascii_lowercase
    return ''.join(random.choice(chars) for x in range(0,Length))


if 0<int(Total)<21:
    while int(Total)>0:
        
        if HasCapital==True and HasLower==True and HasNumbers==True:
            print(randompassword(Length))
            Total=Total-1
            continue
        elif HasCapital==True and HasLower==True and HasNumbers==False:
            print(randomalphapassword(Length))
            Total=Total-1
        elif HasCapital==True and HasLower==False and HasNumbers==False:
            print(randomcapitalpassword(Length))
            Total=Total-1
        elif HasCapital==False and HasLower==True and HasNumbers==False:
            print(randomlowerpassword(Length))
            Total=Total-1
        elif HasCapital==False and HasLower==False and HasNumbers==True:
            print(randomnumericpassword(Length))
            Total=Total-1
        elif HasCapital==True and HasLower==False and HasNumbers==True:
            print(randomcapitalnumberspassword(Length))
            Total=Total-1
        else:
            print("Sorry, you need to have at least one type of character")
    else:
        "The number of passwords is too low or high."


