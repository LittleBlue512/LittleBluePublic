"""
Write a function named sweet to take 2 filenames:
one is for a sweetness table and
another one is for sweeteners in a drink.
The function calculates estimated sweetness of the drink
comparable to 10% sucrose solution,
and appends its calculate to the end of the second file
---the drink-sweetener file.
"""

def sweet(fsweet, fdrink):

    # Retrieve sweetness dict
    sweetness = {}

    # Write your code!

    # Print to check if we retrieve it ok.
    # hint: having a number as float is more convenient later
    # print(sweetness)

    # Calculate the estimated sweetness
    sweet_sum = 0


    # write/append message to the end of file
    msg = "\nSweet as {:.1f}% sucrose solution".format(sweet_sum)

if __name__ == '__main__':
    sweet('sweetness1.txt', 'CocaPanda.txt')