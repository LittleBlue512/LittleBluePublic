"""
Chattipoom Sirimul
623040132-7
P5
"""


def fav_movies():
    res = dict()
    while True:
        movie = input('Movie: ')
        if movie == '':
            break
        comment = input('* Comment: ')
        res[movie] = comment
    return res


if __name__ == '__main__':
    res = fav_movies()
    print(res)
