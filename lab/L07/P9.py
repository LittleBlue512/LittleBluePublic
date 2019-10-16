
def sailor(data):
    minutes = data['H']*60 + data['M']
    meridiem = data['am/pm']
    if meridiem == 'am':
        minutes = 720 - minutes
    angle = minutes/4
    if meridiem == 'am':
        direction = 'East'
    else:
        direction = 'West'
    if angle > 180:
        angle -= 180
        if direction == 'East':
            direction = 'West'
        else:
            direction = 'East'
    return angle, direction


if __name__ == '__main__':
    r = sailor({'H': 5, 'M': 16, 'am/pm': 'am'})
    print(r)
    r = sailor({'H': 11, 'M': 0, 'am/pm': 'am'})
    print(r)
    r = sailor({'H': 12, 'M': 8, 'am/pm': 'pm'})
    print(r)
    r = sailor({'H': 7, 'M': 0, 'am/pm': 'pm'})
    print(r)
    r = sailor({'H': 0, 'M': 0, 'am/pm': 'am'})
    print(r)
    r = sailor({'H': 0, 'M': 4, 'am/pm': 'am'})
    print(r)
