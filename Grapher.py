import matplotlib.pyplot as plt

contestants = ["Miller", "Fanelli", "Mason", "Strat", "Bunboy", "Angie", "Dizzy", "John", "Jack", "Nathan", "Kyle", "Andrea"]
votes = [0,0,0,0,0,0,0,0,0,0,0,0]

import csv
with open('Minecraft Survivor_ Sherwood Fan Favorite Poll (Responses) - Form Responses 1.csv', 'r') as file:
    reader = csv.reader(file)
    allVotes = []
    for row in reader:
        tokens = row[1].split(', ')
        for currToken in tokens:
            allVotes.append(currToken)

    allVotes = allVotes[1:]
    print(allVotes)

    for currVote in allVotes:
        i = 0
        for currCont in contestants:
            if currCont == currVote:
                votes[i] = votes[i] + 1
                #print("test")
            i = i + 1

i = 0
for person in contestants:
    print(person + ": " + str(votes[i]) + " votes")
    i = i + 1

#plt.bar(contestants, votes, label="Fan Favorite Votes - Sherwood")

plt.xlabel('Contestant')
plt.ylabel('Vote Count')
plt.title('Fan Favorite Votes - Sherwood')

xlocs, xlabs = plt.xticks()
xlocs=[i+1 for i in range(0,10)]
xlabs=[i/2 for i in range(0,10)]

bars = plt.bar(contestants, height=votes, width=.8, color=('g'))
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + .25, yval + .005, yval)
'''yval = bar.get_height()
for i, v in enumerate(yval):
    plt.text(xlocs[i] - 0.25, v + 0.01, str(v))'''
plt.show()
