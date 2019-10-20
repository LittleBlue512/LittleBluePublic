
def is_valid(s):
    idx1 = s.find('_')
    idx2 = s.find('.')
    if idx1 != 3 or idx2 != 14:
        return False
    # check topic
    topic = s[:idx1]
    if len(topic) != 3 or topic[0] != 't' or not topic[1].isnumeric() or not topic[2].isnumeric():
        return False
    # check student id
    id = s[idx1+1: idx2]
    if len(id) != 10:
        return False
    for c in id:
        if not c.isnumeric():
            return False
    # check file extension
    ext = s[idx2:]
    if ext != '.tar':
        return False
    return True


if __name__ == '__main__':
    r = is_valid('t05_6210112341.tar')
    print(r)
    print(type(r))
    r = is_valid('t5_621011234-1.zip')
    print(r)
    r = is_valid('T5_621011234-1.zip')
    print(r)
