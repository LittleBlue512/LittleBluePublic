# Return dictionary containing { Bond:str => Energy:int }
def getBondEnergy(bondEnergy):
    res = dict()
    with open(bondEnergy, 'r') as file:
        for line in file:
            e = [x.rstrip() for x in line.split(' ')]
            res[e[0]] = int(e[1])
    return res


# Return list of substrates and list of products
# ['{cnt1}', '{substrate1}', '{cnt2}', '{substrate2}', ...]
# ['{cnt1}', '{product1}', '{cnt2}', '{produc2t}', ...]
def getBondReaction(reaction):
    res, skipFirstLine = list(), True
    with open(reaction, 'r') as file:
        for line in file:
            if(skipFirstLine):
                skipFirstLine = False
            else:
                e = [x.rstrip() for x in line.split(' ')]
                e.remove('+')
                res.append(e)
    return res[0], res[1]


def fire(bondEnergy, reaction):
    bondTable = getBondEnergy(bondEnergy)
    substrate, product = getBondReaction(reaction)
    E1, E2 = 0, 0
    for i in range(1, len(substrate), 2):
        E1 += bondTable[substrate[i]] * int(substrate[i-1])
    for i in range(1, len(product), 2):
        E2 += bondTable[product[i]] * int(product[i-1])
    with open(reaction, 'a') as file:
        file.write('\nEa = {:,.1f} kJ, Er = {:,.1f} kJ, E = {:,.1f} kJ'.format(E1, E2, E1-E2))


if __name__ == '__main__':
    fire('bond_energy.txt', 'methane.txt')
