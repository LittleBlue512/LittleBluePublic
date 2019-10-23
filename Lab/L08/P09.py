"""
Write a function named sweet to take 2 filenames:
one is for a sweetness table and
another one is for sweeteners in a drink.
The function calculates estimated sweetness of the drink
comparable to 10% sucrose solution,
and appends its calculate to the end of the second file
---the drink-sweetener file.
"""


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
    table, drink, totalSweetness = getTable(tableFileName), getDrink(drinkFileName), 0
    totalSweetness = sum([amount * table[sugar] for sugar, amount in drink.items()])
    with open(drinkFileName, 'a') as file:
        file.write("\nSweet as {:.1f}% sucrose solution".format(totalSweetness))


if __name__ == '__main__':
    sweet('sweetness1.txt', 'CocaPanda.txt')
