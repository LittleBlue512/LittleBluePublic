"""
Student's name: Chattipoom Sirimul
id: 623040132-7
""" 

if __name__ == '__main__':
    _sum = 0
    while True:
        val = int(input("value:"))
        _sum += val
        if val == 0:
            break

    print("Summation = {}".format(_sum))