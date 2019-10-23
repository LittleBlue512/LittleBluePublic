def read_vec(fileName):
    res = list()
    with open(fileName, 'r') as file:
        for line in file:
            res.append(int(line.rstrip()))
    return res


if __name__ == '__main__':
    v = read_vec('vec.txt')
    print(v)
