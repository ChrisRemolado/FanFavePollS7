import matplotlib.pyplot as plt
import csv
from Contestant import Contestant

#Set up variables
contestants = [Contestant("Hannah",0,0,0,0), Contestant("Asher",0,0,0,0), Contestant("Joseph",0,0,0,0), Contestant("Chase",0,0,0,0),
               Contestant("Marty",0,0,0,0), Contestant("Liz",0,0,0,0), Contestant("Ben",0,0,0,0), Contestant("Huffle",0,0,0,0),
               Contestant("Timmmeh",0,0,0,0), Contestant("Jay",0,0,0,0), Contestant("Garrett",0,0,0,0), Contestant("CAAJBE",0,0,0,0),
               Contestant("Knife",0,0,0,0), Contestant("Killer",0,0,0,0), Contestant("Corcaigher",0,0,0,0), Contestant("Trevor",0,0,0,0)]

#Open CSV & Tokenize each vote total
#FIRST PLACE VOTES CALCULATIONS
with open('Minecraft Survivor_ Caribbean Fan Favorite Poll (Responses) - Form Responses 1.csv', 'r') as file:
    reader = csv.reader(file)
    tokensList = []
    for line in reader:
        if line[5] != '/':
            tokensList.append(line[2])

    del tokensList[0] #removes header row
    for currToken in tokensList:
        print(tokensList)
        for currContestant in contestants:
            if currContestant.name == currToken:
                currContestant.add_firstVotes()

#SECOND PLACE VOTES CALCULATIONS
with open('Minecraft Survivor_ Caribbean Fan Favorite Poll (Responses) - Form Responses 1.csv', 'r') as file:
    reader = csv.reader(file)
    tokensList = []
    for line in reader:
        if line[5] != '/':
            tokensList.append(line[3])

    del tokensList[0] #removes header row
    for currToken in tokensList:
        print(tokensList)
        for currContestant in contestants:
            if currContestant.name == currToken:
                currContestant.add_secondVotes()

#THIRD PLACE VOTES CALCULATIONS
with open('Minecraft Survivor_ Caribbean Fan Favorite Poll (Responses) - Form Responses 1.csv', 'r') as file:
    reader = csv.reader(file)
    tokensList = []
    for line in reader:
        if line[5] != '/':
            tokensList.append(line[4])

    del tokensList[0] #removes header row
    for currToken in tokensList:
        print(tokensList)
        for currContestant in contestants:
            if currContestant.name == currToken:
                currContestant.add_thirdVotes()

#SORT BARS BY ASCENDING ORDER
totalVotes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(16):
    contestants[i].add_totalVotes()
    totalVotes[i] = contestants[i].totalVotes

n = len(contestants) # Traverse through all array elements - BUBBLE SORT O(n^2)
for i in range(n - 1):
    # range(n) also work but outer loop will repeat one time more than needed.
    # Last i elements are already in place
    for j in range(0, n - i - 1):
        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        if contestants[j].totalVotes > contestants[j + 1].totalVotes:
            contestants[j], contestants[j + 1] = contestants[j + 1], contestants[j]

#Get contestant names & vote total arrays from Contestant objects
cNames = ["","","","","","","","","","","","","","","",""]
for i in range(16):
    cNames[i] = contestants[i].name

firstThreshold = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(16):
    firstThreshold[i] = contestants[i].firstVotes

secondThreshold = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(16):
    secondThreshold[i] = contestants[i].secondVotes + contestants[i].firstVotes

thirdThreshold = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(16):
    thirdThreshold[i] = contestants[i].thirdVotes + contestants[i].secondVotes + contestants[i].firstVotes

#Display graph with each vote total
plt.xlabel('Contestant')
plt.ylabel('Vote Count')
plt.title('Fan Favorite Votes - Caribbean')

xlocs, xlabs = plt.xticks()
xlocs=[i+1 for i in range(0,10)]
xlabs=[i/2 for i in range(0,10)]

bars1 = plt.bar(cNames, height=thirdThreshold, width=.8, color=('#ffa024'), label='3rd favorite')
for bar in bars1:
    yval = bar.get_height()
    plt.text(bar.get_x() + .25, yval + .005, yval)
bars2 = plt.bar(cNames, height=secondThreshold, width=.8, color=('#f2e4aa'), label='2nd favorite')
for bar in bars2:
    yval = bar.get_height()
    #plt.text(bar.get_x() + .25, yval + .005, yval)
bars3 = plt.bar(cNames, height=firstThreshold, width=.8, color=('#10cbe8'), label='1st favorite')
for bar in bars3:
    yval = bar.get_height()
    #plt.text(bar.get_x() + .25, yval + .005, yval)
plt.legend()
plt.show()
