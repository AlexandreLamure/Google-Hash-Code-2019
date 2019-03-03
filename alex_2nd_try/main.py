#!/usr/bin/env python3

import sys
import os
import time
from solve import *

def parse():
    filein = sys.argv[1] # get filename
    tab = []

    lines = [line.rstrip('\n') for line in open(filein)]

    lines = lines[1:] # remove parameters line from tab
    for line in lines:
        tab.append(line.split(' '))

    return tab

def print_parse(tab):
    for line in tab:
        print(line)

def save(solution, score):
    returnString = str(len(solution))
    returnString += '\n'
    for e in solution:
        returnString += e[0] + '\n'

    if not os.path.exists("results"):
        os.makedirs("results")
    filename = "result__" + str(score) + '__' + str(time.time()) + ".txt"
    fichier = open("results/" + filename, "w")
    fichier.write(returnString)
    fichier.close()
    print('NEW SCORE !!')
    print('Saving results to results/' + filename)

def compute_score(solution):
    score = 0
    for i in range(len(solution) - 1):
        tags = solution[i][1][2:]
        tags_next = solution[i+1][1][2:]
        common = len(set(tags).intersection(tags_next))
        score += min(common, len(tags) - common, len(tags_next) - common) 
    return score

def main():
    score = 0
    tab = parse()
    print_parse(tab)
    while(True):
        solution = solve(tab)
        new_score = compute_score(solution)
        if (new_score > score):
            score = new_score
            save(solution, score)

if __name__ == "__main__":
    main()
