

def typhoon(w_spd, a_dst, area, height):
    if w_spd >= 252:
        t = 'Category 5'
    elif w_spd >= 209:
        t = 'Category 4'
    elif w_spd >= 178:
        t = 'Category 3'
    elif w_spd >= 155:
        t = 'Category 2'
    elif w_spd >= 119:
        t = 'Category 1'
    elif w_spd >= 63:
        t = 'Tropical Storm'
    else:
        t = 'Tropical Depression'
    w_spd *= 1000/3600
    area *= 1000**2
    m = a_dst * area * height
    e = 0.5*m*w_spd**2
    return [t, e]


if __name__ == '__main__':
    res = typhoon(55, 1.225, 80424, 15240)
    print(res)

    res = typhoon(200, 1.225, 80424, 15240)
    print(res)
