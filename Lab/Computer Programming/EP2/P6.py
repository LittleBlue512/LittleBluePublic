"""
Chattipoom Sirimul
623040132-7
P6
"""


def simple_poet(fileName):
    res = list()
    with open(fileName, 'r') as file:
        for line in file:
            res.append(line.strip())
    return res


if __name__ == '__main__':
    res = simple_poet('poem.txt')
    print(res)
