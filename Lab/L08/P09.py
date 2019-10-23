def getTable(tableFileName):
    table, skipFirstLine = dict(), True
    with open(tableFileName, 'r') as file:
        for line in file:
            e = line.split(' ')
            if (skipFirstLine):
                skipFirstLine = False
            else:
                table[e[0]] = float(e[1])
    return table


def getDrink(drinkFileName):
    drink = dict()
    with open(drinkFileName, 'r') as file:
        for line in file:
            e = line.split(' ')
            drink[e[0]] = float(e[1])
    return drink


def sweet(tableFileName, drinkFileName):
    table, drink, totalSweetness = getTable(
        tableFileName), getDrink(drinkFileName), 0
    totalSweetness = sum([amount * table[sugar]
                          for sugar, amount in drink.items()])
    with open(drinkFileName, 'a') as file:
        file.write('\nSweet as {}% sucrose solution'.format(totalSweetness))


if __name__ == '__main__':
    sweet('sweetness1.txt', 'Cocapanda.txt')
