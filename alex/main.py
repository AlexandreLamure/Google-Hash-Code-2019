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

def save(solution):
    returnString = str(len(solution))
    returnString += '\n'
    for e in solution:
        returnString += str(e) + '\n'

    if not os.path.exists("results"):
        os.makedirs("results")
    filename = "result_" + str(time.time()) + ".txt"
    fichier = open("results/" + filename, "w")
    fichier.write(returnString)
    fichier.close()
    print('Saving results to results/' + filename)


def main():
    tab = parse();
    #print_parse(tab);
    solution = solve(tab);
    print_solve();
    save(solution);

if __name__ == "__main__":
    main()
