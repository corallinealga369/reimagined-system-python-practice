import sys
import random

results = []



#for $rolls roll a die with values between 1 and the number of side
for x in range(int(sys.argv[1])):
    
    results.append(random.randint(1,int(sys.argv[2])))

if len(sys.argv) == 4:
    if sys.argv[3] == 's' or 'S':
       sortedresults=sorted(results)
       print(sortedresults)
    else: 
        print(results)
else:
    print(results)

