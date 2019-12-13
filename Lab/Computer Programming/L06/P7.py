
def collect_data():
    _name = list()
    _cnt = list()
    while(True):
        name = input("Observation:")
        if name == '':
            return _name, _cnt
        cnt = int(input("Found:"))
        _name.append(name)
        _cnt.append(cnt)


if __name__ == '__main__':
    observ, counting = collect_data()
    print(observ)
    print(counting)
