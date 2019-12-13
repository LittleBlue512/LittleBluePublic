"""
Chattipoom Sirimul
623040132-7
P3
"""


def head_tail(text):
    return (text[0], text[1:])


if __name__ == '__main__':
    res = head_tail("Python")
    print(res)
    res = head_tail("ABCDEFGHIJK")
    print(res)
