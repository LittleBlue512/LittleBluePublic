
Ap = ['f/1.4', 'f/2', 'f/2.8', 'f/4', 'f/5.6', 'f/8', 'f/11', 'f/16', 'f/22']
Sh = ['1/4', '1/8', '1/15', '1/30', '1/60', '1/125',
      '1/250', '1/500', '1/1000', '1/2000', '1/4000']
ISO = ['100', '200', '400', '800', '1600', '3200']


def cam_expos(nat, pro):
    res = list()
    res.append(Ap.index(nat[0]) - Ap.index(pro[0]))
    res.append(Sh.index(nat[1]) - Sh.index(pro[1]))
    res.append(- ISO.index(nat[2]) + ISO.index(pro[2]))
    res.append(sum(res))

    return tuple(res)


if __name__ == '__main__':
    res = cam_expos(['f/2.8', '1/500', '400'], ['f/5.6', '1/125', '200'])
    print(res)
