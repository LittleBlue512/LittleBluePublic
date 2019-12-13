
def perf_note(l, n):
    for note in l:
        if n >= note[1] and n <= note[2]:
            return note[0]

    return None


if __name__ == '__main__':
    pnotes = [['head note', 1, 14],
              ['heart note', 15, 60],
              ['base note', 61, 100]]

    note = perf_note(pnotes, 8)
    print(note)
    note = perf_note(pnotes, 34)
    print(note)
    note = perf_note(pnotes, 78)
    print(note)
