

def int2note(num):
    octave = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    return octave[num-1]


if __name__ == '__main__':
    n = int2note(1)
    print(n)
    n = int2note(3)
    print(n)
    n = int2note(5)
    print(n)
    n = int2note(7)
    print(n)
