def read_records(fileNmae):
    res = dict()
    with open(fileNmae, 'r') as file:
        for line in file:
            key, val = line.rstrip().split('=')
            res[key] = val
    return res


if __name__ == '__main__':
    res = read_records('top_NP.txt')
    print(res)
