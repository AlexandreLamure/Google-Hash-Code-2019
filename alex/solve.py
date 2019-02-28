# Solve the problem
def solve(tab):
    for i in range(len(tab)):
        tab[i] = [i] + tab[i]

    big_table = []
    for i in range(len(tab)):
        big_table.append([])
        tags_x = set(tab[i][3:])
        for j in range(len(tab)):
            tags_y = set(tab[j][3:])
            common = len(tags_x.intersection(tags_y))
            big_table[i].append(min(len(tags_x) - common, len(tags_y) - common, common))
        big_table[i][i] = None

    dodge_x = set()
    dodge_y = set()

    entrant = []
    sortant = []
    for i in range(len(tab)):
        tupl = (i, i, [str(i)])
        entrant.append(tupl)
        sortant.append(tupl)


    while len(dodge_x) + 1 < len(sortant):
        max_x = 0
        max_y = 0
        max_delta = 0
        for i in range(len(tab)):
            if i in dodge_x:
                continue
            maxi_y = 0
            maxi = 0
            maxi2 = 0
            for j in range(len(tab)):
                if j in dodge_y:
                    continue
                if tab[i][j] > maxi:
                    maxi2 = maxi
                    maxi_y = j
                    maxi = tab[i][j]
            delta = maxi - maxi2
            if delta > max_delta:
                max_x = i
                max_y = maxi_y
                max_delta = delta

        dodge_x.add(max_x)
        dodge_y.add(max_y)

        sortant[max_x][1] = entrant[max_y][1]
        sortant[max_x][2] += entrant[max_y][2]
        sortant[entrant[max_y][1]] = sortant[max_x]

        big_table[sortant[max_x][1]][sortant[max_x][0]] = None
        #done




    for i in range(len(sortant)):
        if i in dodge_x:
            continue
        return '\n'.join(e for e in sortant[i][2])


# To debug
def print_solve():
    print('-----------DEBUG-----------')

    # FIXME: Write code here

    print('---------------------------')
