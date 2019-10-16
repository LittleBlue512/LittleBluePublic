
def est_prob(_dict):
    total = sum(_dict.values())
    res = dict()
    for k, v in _dict.items():
        res[k] = v/total

    return res


if __name__ == '__main__':
    wcount = {'culinary': 3, 'history': 5, 'dynasty': 1, 'silk': 2,
              'Buddhist': 2, 'caves': 2, 'wall': 3, 'history': 4}
    ps = est_prob(wcount)
    print('Text:', wcount)
    print('Count:', ps)
