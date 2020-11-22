class Contestant(object):
    name = ""
    firstVotes = 0
    secondVotes = 0
    thirdVotes = 0
    totalVotes = 0

    # The class "constructor" - It's actually an initializer
    def __init__(self, name, firstVotes, secondVotes, thirdVotes, totalVotes):
        self.name = name
        self.firstVotes = firstVotes
        self.secondVotes = secondVotes
        self.thirdVotes = thirdVotes
        self.totalVotes = totalVotes

    def add_firstVotes(self):
        self.firstVotes = self.firstVotes + 3

    def add_secondVotes(self):
        self.secondVotes = self.secondVotes + 2

    def add_thirdVotes(self):
        self.thirdVotes = self.thirdVotes + 1

    def add_totalVotes(self):
        self.totalVotes = self.firstVotes + self.secondVotes + self.thirdVotes

def make_contestant(name, firstVotes, secondVotes, thirdVotes, totalVotes):
    contestant = Contestant(name, firstVotes, secondVotes, thirdVotes, totalVotes)
    return contestant