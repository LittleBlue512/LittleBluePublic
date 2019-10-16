
def rational_decision(D, name):
    S = D[name] # Get scenarios of the person.
    minNotConfess = min(S[0]) # not confess
    minConfess = min(S[1]) # confess
    if minNotConfess < minConfess:
        return 0
    return 1

if __name__ == '__main__':
    choices = ['not confess', 'confess']
    s = {'Lobha': [[3, 10], [1, 5]], 'Raga': [[3, 10], [1, 5]]}
    p = 'Lobha'
    r = rational_decision(s, p)
    print(p, ':', choices[r])
