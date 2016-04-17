#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
from copy import copy


#Find where "string" is in first element of list of lists"l"
def where(string,l): 
    for i in range(len(l)):
        if l[i][0]==string: return i

#Find if "elem" is in list "l"
def isin(elem,l):
    return elem in l

#Find if "elem" is in a list of lists"l"
def isinlists(elem,l):
    return elem in [element for sublist in l for element in sublist]

def tree_search():
    frontier = [['Arad']]
    explored = []
    goal = 'Bucharest'

    while 1:
        if frontier==[]: return "Error"
        path, frontier = remove_choice(frontier)
        endnode = path[-1]
        explored.append(endnode)
        if endnode==goal: return path

        #Iterate over all possible actions at endnode
        for action in allactions[where(endnode,allactions)][1::] :
            if not isin(action,explored) and not isinlists(action, frontier) or action==goal:
            #frontier.append([path,action])
            #Flatten list
                pathtem=copy(path)
                pathtem.append(action)
                frontier.append(pathtem)



#breadth-first
def breadth_first(frontier):
    #Calculates the lengths of all paths in frontier, returns the frontier
    #without the shortest path and also returns that path
    lengths = [len(f) for f in frontier]
    shortest=[i for i,l in enumerate(lengths) if l<=min(lengths)]
    return frontier.pop(shortest[0]), frontier 

#uniform cost
def uniform_cost(frontier):
    #Calculates the cost of all paths in frontier, returns the frontier
    #without the lest expensive path and also returns that path
    lengths = [cost(f) for f in frontier]
    shortest=[i for i,l in enumerate(lengths) if l<=min(lengths)]
    return frontier.pop(shortest[0]), frontier 

#depth-first
def depth_first(frontier):
    #Returns the frontier without the first path and also returns that path
    return frontier.pop(0), frontier 

#A*
def a_star(frontier):
    #Calculates the cost added to the heuristic cost of all paths in frontier, returns the frontier
    #without the lest expensive path and also returns that path
    lengths = [cost(f)+h[f[-1]] for f in frontier]
    shortest=[i for i,l in enumerate(lengths) if l<=min(lengths)]
    print lengths
    return frontier.pop(shortest[0]), frontier 

remove_choice = a_star

def cost(path):
    return sum([find_length(path[i],path[i+1]) for i in range(len(path)-1)])

def find_length(c1,c2):
    #Find length between cities "c1" and "c2"
    for pair in data:
        if (pair[0]==c1 or pair[1]==c1) and (pair[0]==c2 or pair[1]==c2):
            return float(pair[2])

filename='romania'
with open(filename,'rb') as f: 
    data = f.read().splitlines()
    data = [l.split() for l in data]



cities = ['Arad','Timisoara','Zerind','Sibiu','Oradea','Fagaras', 'RimnicuVilcea', 'Pitesti','Lugoj','Mehadia','Bucharest']
h = {'Arad':366,'Timisoara':329,'Zerind':374,'Sibiu':253,'Oradea':671,'Fagaras':176,'RimnicuVilcea':193,'Pitesti':100,'Lugoj':244,'Mehadia':241,'Bucharest':0}

#Create list with all possible actions for each city
#The element of each list is the city of origin
allactions=[]
for city in cities:
    actions=[city]
    for d in data:
        if d[0]==city: actions.append(d[1])
        if d[1]==city: actions.append(d[0])
    allactions.append(actions)



sol=tree_search()
print "\n"
print sol

