
def get_dict_val(_dict, k1, k2):
    return (_dict[k1], _dict[k2])


if __name__ == '__main__':
    visits = {'Denali NP': 2007, 'Arequipa': 2006, 'Taktsang': 2015}
    visited = get_dict_val(visits, 'Arequipa', 'Denali NP')
    print(visited)
