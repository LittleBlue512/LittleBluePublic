"""
Student's name: Chattipoom Sirimul
id: 623040132-7
Geometric mean
"""

if __name__ == '__main__':
    n = int(input("How many values?"))
    prod = 1
    for i in range(n):
        val = float(input("value:"))
        prod *= val
    gmean = prod**(1/n)
    # do not edit below this line
    # ===========================================
    print('Geometric mean = {:.6f}'.format(gmean))