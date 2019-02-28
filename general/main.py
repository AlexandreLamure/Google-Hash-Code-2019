#!/usr/bin/env python3

import sys

def parse():
    filein = sys.argv[1] # get filename
    tab = []

    file  = open(filein, "r")
    i = 0
    for line in file:
        tab.append([])
        for char in line:
            if char != '\n':
                tab[i].append(char)
        i += 1
    file.close() 

    param_row = tab[0] # get parameters line
    tab = tab[1:] # remove parameters line from tab
    params = ''.join(param_row).split(' ') # convert chars to strings
    params = list(map(int, params)) # convert strings to ints
    '''
        params is an 1D array of int
        tab is a 2D array of char
    '''
    return params, tab

def print_parse(params, tab):
    print(params)
    for line in tab:
        print(line)

def main():
    (params, tab) = parse();
    print_parse(params, tab);
    #solve(params, tab);
    #print_solve();
    #save();

if __name__ == "__main__":
    main()
