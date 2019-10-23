def read_taxo(fileName):
    res = list()
    with open(fileName, 'r') as file:
        for line in file:
            res.append(line.rstrip())
    return res


if __name__ == '__main__':
    res = read_taxo('whales.txt')
    print(res)
