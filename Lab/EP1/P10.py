"""
Student's name: Chattipoom Sirimul
id: 623040132-7
"""

if __name__ == '__main__':
    n = int(input("Enter a number of values:"))
    res = 0
    cnt = 1
    while cnt <= n:
        val = int(input("value:"))
        res += val
        cnt += 1

    print("Summation =", res)
