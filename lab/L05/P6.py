
def find_key(s, key):
    return s.find(key)

if __name__ == '__main__':
    r = find_key("For benefits and happiness of us all till the end of time",
                 "happiness")
    print(r)
    r = find_key("For benefits and happiness of us all till the end of time",
                 "courage")
    print(r)
    r = find_key("For benefits and happiness of us all till the end of time",
                 "of")
    print(r)
