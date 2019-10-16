
def have_visited(_dict, k):
    return True if k in _dict.keys() else False


if __name__ == '__main__':
    visits = {'Denali NP': 2007, 'Arequipa': 2006, 'Taktsang': 2015}
    visited = have_visited(visits, 'Taktsang')
    print(visited)
