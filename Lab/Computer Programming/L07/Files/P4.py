
def add_place(_dict, k, val):
    _dict[k] = val
    return _dict


if __name__ == '__main__':
    visits = {'Denali NP': 2007, 'Arequipa': 2006, 'Taktsang': 2015}
    visits = add_place(visits, 'Taktsang', 2014)
    print(visits)
    visits = add_place(visits, 'Provins', 2013)
    print(visits)
