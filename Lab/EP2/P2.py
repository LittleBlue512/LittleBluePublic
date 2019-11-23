"""
Chattipoom Sirimul
623040132-7
P2
"""


def thresholding(threshold, val):
    if val > threshold:
        return 'yes'
    return 'no'


if __name__ == '__main__':
    res = thresholding(1.8, 1.6)
    print(res)
    res = thresholding(2.8, 2.8)
    print(res)
    res = thresholding(4.8, 5)
    print(res)
