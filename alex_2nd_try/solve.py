import random

# Solve the problem
def solve(tab):
    id_tab = []
    for i in range(len(tab)):
        id_row = []
        id_row.append(str(i))
        id_row.append(tab[i])
        id_tab.append(id_row)
    #print_tab(id_tab)
    random.shuffle(id_tab)
    #print_tab(id_tab)
    id_tab2 = []
    to_skip = set()
    for i in range(len(id_tab)):
        if i in to_skip:
            continue
        if id_tab[i][1][0] == 'H':
            id_tab2.append(id_tab[i])
        else:
            for j in range(i+1, min(len(id_tab), i+10)):
                if id_tab[j][1][0] == 'V':
                    id_tab2.append(id_tab[i])
                    id_tab2[-1][0] += ' ' + id_tab[j][0] # merge ids
                    id_tab2[-1][1].extend(id_tab[j][1][2:]) # merge tags
                    to_skip.add(j)
                    break
                
    return id_tab2

# To debug
def print_tab(tab):
    print('-----------DEBUG-----------')
    for line in tab:
        print(line)
    print('---------------------------')
