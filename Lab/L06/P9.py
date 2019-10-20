
def laplace_smooth(l, a):
    total = sum(l)
    for i in range(len(l)):
        l[i] = (l[i] + a)/(total + a*len(l))

    return l

if __name__ == '__main__':
    counting = [0, 8, 20, 4, 12]
    res = laplace_smooth(counting, 0.1)
    print(res)