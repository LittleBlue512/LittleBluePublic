import math

def cos_sim(l1, l2):
    a, b, c = 0, 0, 0
    for i in range(len(l1)):
        a += l1[i] * l2[i]
        b += l1[i]**2
        c += l2[i]**2

    return a / (math.sqrt(b) * math.sqrt(c))


if __name__ == '__main__':
    cs = cos_sim([1, 0], [5, 5])
    print(cs)

    cs = cos_sim([14, 0, 5], [5, 8, 4])
    print(cs)
