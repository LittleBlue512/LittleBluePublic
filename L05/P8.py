
def k2k(s, k1, k2):
    idx1 = s.find(k1)
    idx2 = s.find(k2)
    if idx1 == -1 or idx2 == -1:
        return ''
    if idx1 < idx2:
        return s[idx1:idx2+len(k2)]
    else:
        return s[idx2:idx1+len(k1)]


if __name__ == '__main__':
    r = k2k('Life is not a game to win, but a melange of lessons to learn.',
            'game', 'Life')
    print(r)
    r = k2k('Life is not a game to win, but a melange of lessons to learn.',
            'not', 'win')
    print(r)
    r = k2k('Life is not a game to win, but a melange of lessons to learn.',
            'win', 'not')
    print(r)
    r = k2k('Life is not a game to win, but a melange of lessons to learn.',
            'live', 'learn')
    print(r)
    r = k2k('Life is not a game to win, but a melange of lessons to learn.',
            'but', 'lessons')
    print(r)
    r = k2k('Life is not a game to win, but a melange of lessons to learn.',
            'lessons', 'learn')
    print(r)
