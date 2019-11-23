"""
Chattipoom Sirimul
623040132-7
P4
"""


def head_mid_tail(_list):
    return (_list[0], _list[1:-1], _list[-1])


if __name__ == '__main__':
    testlist = [11, 38, 4, 5, 2]
    res = head_mid_tail(testlist)
    print(res)
    testlist = ["Relax", "Tense brain does not work well",
                "Smile eases the tension"]
    res = head_mid_tail(testlist)
    print(res)
