
def getBondEnergy(bondEnergy):
    res = dict()
    with open(bondEnergy, 'r') as file:
        for line in file:
            e = [x.rstrip() for x in line.split(' ')]
            res[e[0]] = int(e[1])
    return res


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
    Ea, Er = 0, 0
    for i in range(1, len(substrate), 2):
        Ea += bondTable[substrate[i]] * int(substrate[i-1])
    for i in range(1, len(product), 2):
        Er += bondTable[product[i]] * int(product[i-1])
    with open(reaction, 'a') as file:
        file.write('\nEa = {} kJ, Er = {} kJ, E = {} kJ'.format(float(Ea), float(Er), float(Ea) - float(Er)))


if __name__ == '__main__':
    fire('bond_energy.txt', 'methane.txt')
