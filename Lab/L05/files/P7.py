
def to_key(s, key):
    idx = s.find(key)
    if idx == -1:
        return ''
    return s[:s.find(key)+len(key)]

if __name__ == '__main__':
    r = to_key('For benefits and happiness of us all till the end of time', 'happiness')
    print(r)
    r = to_key('For benefits and happiness of us all till the end of time', 'of')
    print(r)
    r = to_key('For benefits and happiness of us all till the end of time', 'wisdom')
    print(r)
    r = to_key('For benefits and happiness of us all till the end of time', 'For')
    print(r)
