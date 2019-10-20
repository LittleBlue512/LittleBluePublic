
def vec_add(l1, l2):
    if len(l1) != len(l2):
        return []
    res = list()
    for i in range(len(l1)):
        res.append(l1[i] + l2[i])

    return res


if __name__ == '__main__':
    v1 = [1, 7, 8, -5]
    v2 = [3, 2, 6, 12]
    vc = vec_add(v1, v2)
    print(vc)

    v1 = [10, 13, 28, 5, 0]
    v2 = [3, 2, 6, 12]
    vc = vec_add(v1, v2)
    print(vc)

    v1 = [10, 13, 28, 5, 0]
    v2 = [3, 2, 6, 12, -4]
    vc = vec_add(v1, v2)
    print(vc)
