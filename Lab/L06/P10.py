
def earthquake(l):
    for i in range(len(l)):
        l[i].append(10**(4.8 + 1.5*l[i][1]))

    return l


if __name__ == '__main__':
    events = [['2019 02 22 Ecuador', 7.5],
              ['2018 08 19 Fiji', 8.2],
              ['2017 09 08 Mexico', 8.2]]
    res = earthquake(events)
    print(res)
