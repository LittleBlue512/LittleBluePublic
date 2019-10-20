def grow_list(l, item):
    l.append(item)
    return l


if __name__ == '__main__':
    res = grow_list([2, 4, 8, 16], 32)
    print(res)
