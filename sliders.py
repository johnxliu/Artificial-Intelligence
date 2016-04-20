#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import random
from copy import copy, deepcopy


def tree_search():
    game = SlidingBlocks(4)
    game.shuffle(10)

    frontier = [[game]]
    explored = []

    while 1:
        if frontier == []:
            return "Error"

        path, frontier = remove_choice(frontier)
        endnode = path[-1]
        explored.append(endnode)
        if endnode.is_win():
            return path

        #Iterate over all possible actions at endnode
        for action in allactions(endnode):
            if action not in explored and action not in frontier or action.is_win():
                pathtem = copy(path)
                pathtem.append(action)
                frontier.append(pathtem)


def allactions(obj):
    possible = obj.find_moves()
    actions = []
    for i, pos in enumerate(possible):
        actions.append(deepcopy(obj))
        actions[i].move(pos)
    return actions


# breadth-first
def breadth_first(frontier):
    """
    Calculates the lengths of all paths in frontier, returns the frontier
    without the shortest path and also returns that path
    """

    lengths = [len(f) for f in frontier]
    shortest = [i for i, l in enumerate(lengths) if l <= min(lengths)]
    return frontier.pop(shortest[0]), frontier


# depth-first
def depth_first(frontier):
    """
    Returns the frontier without the first path and also returns that path
    """
    return frontier.pop(0), frontier


# A*
def a_star(frontier):
    """
    Calculates the cost added to the heuristic cost of all paths in frontier, returns the frontier
    without the lest expensive path and also returns that path
    """

    lengths = [f[-1].total_misplaced() + cost(f) for f in frontier]
    minlen = min(lengths)
    shortest = [i for i, l in enumerate(lengths) if l <= minlen]
    return frontier.pop(shortest[0]), frontier


def cost(path):
    return len(path)


class SlidingBlocks():

    def __init__(self, size=3):
        self.size = size
        self.block = self.generate_block()

    def generate_block(self):
        """Goal state"""

        block = np.arange(1, self.size**2)
        block.resize(self.size, self.size)
        return block

    def move(self, piece):
        """Moves the piece with index "piece" (as tuple) to free place, if possible """

        if piece not in self.find_moves():
            return "error"
        else:
            self.block[self.find_free()] = self.block[piece]
            self.block[piece] = 0
            return "success"

    def find_free(self):
        """Returns array of indices free cell"""

        free_position = np.where(self.block == 0)
        return free_position

    def find_moves(self):
        """Returns list of allowed indices to move"""

        from itertools import product
        free_position = np.array(self.find_free()).flatten()
        allowed_displacements = [[0,1],[1,0],[-1,0],[0,-1]]
        return [tuple(free_position + d) for d in allowed_displacements if
                tuple((free_position + d).tolist()) in product(range(self.size), repeat=2)]

    def shuffle(self, steps=10):
        for i in xrange(steps):
            self.rand_move()

    def rand_move(self):

        self.move(random.choice(self.find_moves()))

    # The following functions are used to find the solution

    def is_win(self):
        return (self.block == self.generate_block()).all()


    def taxicab_distance(self, piece1, piece2):
        piece1, piece2 = np.array(piece1), np.array(piece2)
        return sum(abs(piece1 - piece2))

    def distance(self):
        from itertools import product

        goal = self.generate_block()
        distances = np.array([self.taxicab_distance(ind, np.where(goal==self.block[ind])) for ind in product(range(4),repeat=2)])
        distances.resize(4,4)
        return distances

    def total_misplaced(self):
        return np.sum( self.block != self.generate_block() )


if __name__ == "__main__":

    remove_choice = a_star

    sol = tree_search()
    for s in sol:
        print s.block

# import os
# from time import sleep
# def clear(): os.system('cls' if os.name == 'nt' else 'clear')
#
# game = SlidingBlocks()
# game.shuffle()
#
# while not game.is_win():
#     clear()
#     print game.block
#     print "Select block to move:"
#     ind = raw_input()
#     ind = tuple([float(i) for i in ind.split(',')])
#     print game.move(ind)
#
#
# def move_to(self, piece, direction):
#     from itertools import product
#     piece = np.array(piece)
#     directions = {"up": [-1,0], "down": [1,0], "left": [0,-1], "right": [0,1]}
#
#     #Check if moving to occupien place or out of bounds
#     if tuple(piece+directions[direction]) not in product(range(4),repeat=2) or self.block[tuple(piece+directions[direction])] != 0 :
#         print "error"
#     else:
#         self.block[tuple(piece+directions[direction])] = self.block[tuple(piece)]
#         self.block[tuple(piece)] = 0
