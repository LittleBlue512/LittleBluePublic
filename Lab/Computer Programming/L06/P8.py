
def est_prob(l):
    total = sum(l)
    for i in range(len(l)):
        l[i] /= total
    return l


if __name__ == '__main__':
    counting = [0, 8, 20, 4, 12]
    res = est_prob(counting)
    print(res)
