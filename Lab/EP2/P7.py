"""
Chattipoom Sirimul
623040132-7
P7
"""


def write_list(fileName, _list):
    with open(fileName, 'w') as file:
        for e in _list:
            file.write(e + '\n')


if __name__ == '__main__':
    serengeti_rules = ['keystone species', 'density regulation',
                       'trophic cascade', 'nature resilience']
    write_list('srules.txt', serengeti_rules)
