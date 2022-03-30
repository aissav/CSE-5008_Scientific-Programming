'''
Rock-Paper-Scissors game
Starter code for Stanford CME 193
author: Sven Schmit
'''

import random

class Agent:
    def getMove(self, moves_other, moves_self):
        pass


class InstructorAgent(Agent):
    def __init__(self):
        p_rock = random.random()
        p_scissors = random.random()
        p_paper = random.random()
        p_total = p_rock + p_scissors + p_paper

        self.p_rock = p_rock / p_total
        self.p_scissors = self.p_rock + p_scissors / p_total

    def getMove(self, moves_other, moves_self):
        random_move = random.random()
        if random_move < self.p_rock:
            return 'r'
        elif random_move < self.p_scissors:
            return 's'
        else:
            return 'p'


class MyAgent(Agent):
    def __init__(self):
        p_rock = random.random()
        p_scissors = random.random()
        p_paper = random.random()
        #add weights to the total value
        #since rock has a great oppurtunity, then i assign a wight of 2
        p_total = 2*p_rock + p_scissors + 0.5 * p_paper

        #give high oppurtunity to the rock move
        self.p_rock = 2*(p_paper) / p_total
        self.p_scissors = self.p_rock + p_scissors / p_total
        self.p_paper=0.05
        #it beats the other agents in most of the epochs

    def getMove(self, moves_other, moves_self):

        random_move = random.random()
        if random_move < self.p_rock:
            return 'r'
        elif random_move < self.p_scissors:
            return 's'
        else:
            return 'p'


class HumanAgent(Agent):
    def getMove(self, moves_other, moves_self):

        # YOUR CODE HERE
        while True:
            user=raw_input("Please input the next move: ")
            if user=='r' or user =='p' or user=='s':
                return user
            else:
                print("Error Input!")
