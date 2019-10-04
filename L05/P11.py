
def sailor_mate(w, s):  # w -> wind, s -> sail
    w = int(w[:w.find(':')])*30 + int(w[w.find(':')+1:])*0.50
    s = int(s[:s.find(':')])*30 + int(s[s.find(':')+1:])*0.50
    diff = abs(w - 180)
    if w > 180:
        w -= diff
        s -= diff
        if s < 0:
            s += 360
    else:
        w += diff
        s += diff
        if s > 360:
            s %= 360
    res = ''
    if s == w:
        res += 'run'
    else:
        if abs(s - w) >= 180 - 45:
            res += 'tacking'
        else:
            if s > w:
                res += 'starboard'
            if s < w:
                res += 'port'
            if abs(s - w) > 90:
                res += ' close hauled'
            elif abs(s - w) == 90:
                res += ' beam reach'
            elif abs(s - w) > 0:
                res += ' broad reach'
            elif s == w:
                res = 'running'
    return res


if __name__ == '__main__':
    r = sailor_mate("9:00", "12:00")
    print("9:00", "12:00", r)
    ticks = ["12:00", "1:30", "1:31", "2:59", "3:00",
             "3:01", "5:59", "6:00", "6:01", "8:59", "9:00", "9:01",
             "10:29", "10:30"]
    for b in ticks:
        r = sailor_mate("6:00", b)
        print("6:00", b, r)
