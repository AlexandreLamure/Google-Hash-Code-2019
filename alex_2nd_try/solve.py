import random

# Solve the problem
def solve(tab):
    id_tab = []
    for i in range(len(tab)):
        id_row = []
        id_row.append(i)
        id_row.append(tab[i])
        id_tab.append(id_row)
    print_tab(id_tab)
    random.shuffle(id_tab)
    print_tab(id_tab)
    return id_tab

# To debug
def print_tab(tab):
    print('-----------DEBUG-----------')
    for line in tab:
        print(line)
    print('---------------------------')
