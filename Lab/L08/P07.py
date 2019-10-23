def read_mat(fileName):
    res = list()
    with open(fileName, 'r') as file:
        for line in file:
            res.append([int(x.rstrip()) for x in line.split(' ')])
    return res


if __name__ == '__main__':
    res = read_mat('mat0.txt')
    print(res)
