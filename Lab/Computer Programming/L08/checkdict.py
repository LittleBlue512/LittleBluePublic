"""
Utilities for autograding dictionary answer
"""

def check_dict(d, f=lambda x: x):
    dkeys = list(d.keys())
    dkeys.sort()

    for k in dkeys:
        print(k, f(d[k]), end='; ')

    print()


def sorted_keys(d):
    dkeys = list(d.keys())
    dkeys.sort()

    return dkeys


if __name__ == '__main__':
    stay = {'USA': 3000, 'Peru': 14, 'France': 5, 'Italy': 7}

    check_dict(stay)

    frac = {'N Am': 3.45, 'S Am': 8.33, 'Carib': 1.77, 'Pac': 1.02}

    check_dict(frac, lambda x: round(x,1))