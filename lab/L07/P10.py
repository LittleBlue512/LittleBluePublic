
def rational_decision(D, name):
    S = D[name]  # Get scenarios of the person.
    p = [0, 0]
    p[0 if S[0][0] < S[1][0] else 1] += 1
    p[0 if S[0][1] < S[1][1] else 1] += 1
    if p[0] > p[1]:
        return 0
    if p[1] > p[0]:
        return 1
    return None


if __name__ == '__main__':
    choices = ['not confess', 'confess']
    s = {'Lobha': [[3, 10], [1, 5]], 'Raga': [[3, 10], [1, 5]]}
    p = 'Lobha'
    r = rational_decision(s, p)
    print(p, ':', choices[r])
