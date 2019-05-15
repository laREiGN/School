###     Analysis 3, INF1H
###     Girts Dvinskis, 0967963     //    Tim Wolcken, 0896457
###     The Game of Pig

import random as r

turnnumber = 1

class player:
    turnscore = 0
    totalscore = 0
    keep_rolling = True

    def __init__(self, name):
        self.name = name

    def roll_die(self):
        self.outcome = r.randint(1,6)

    def roll(self):
        global turnnumber
        self.roll_die()
        if self.outcome == 1:
            print(self.name, 'has rolled a 1 and misses a turn')
            print('The total score of', self.name, 'is', self.totalscore, '\n')
            self.keep_rolling = False
            self.turnscore = 0
            turnnumber += 1
        else:
            print(self.name, 'has rolled a', self.outcome)
            self.turnscore += self.outcome
            print('Current turn score:', self.turnscore)
            print('The total score of', self.name, 'is', self.totalscore, '\n')
            self.prompt()

    def hold(self):
        self.totalscore += self.turnscore
        self.turnscore = 0
        print('The current score of', self.name, 'is', self.totalscore, '\n')

    def prompt(self):
        global turnnumber
        print(self.name, 'is playing and currently has', self.totalscore, 'points;')
        i = int(input('Press 1 to ROLL or 2 to HOLD:   '))
        print('\n')
        if i == 1:
            self.roll()
        elif i == 2:
            if self.turnscore == 0:
                print('You have not rolled yet.')
                confirmation = int(input('Are you sure you want to hold with no points? Yes: 1, No: 2   :'))
                if confirmation == 1:
                    self.hold()
                elif confirmation == 2:
                    turnnumber += 1
                else:
                    self.prompt()
            else:
                self.hold()
            turnnumber += 1
        else:
            print('Incorrect input. Try again. Tip: enter either 1 or 2', '\n')

class main:
    p = player('Player 1')
    p2 = player('Player 2')
    print('Welcome to our rendition of \n    THE GAME OF PIG! \n')
    global turnnumber
    while p.totalscore < 100 and p2.totalscore < 100:
        if turnnumber % 2 == 0:
            p2.prompt()
        else:
            p.prompt()
    print('The game is over!')
    if p.totalscore >= 100:
        print('Player 1 has won!')
    else:
        print('Player 2 has won!')
main()
