"""
Student's name: Chattipoom Sirimul
id: 623040132-7
P17
Sigmoid
"""

import math

# Write your code here
# ...

def sigmoid(a):
    return 1/(1+math.exp(-a))

# Do not edit below this line
# ===================================
if __name__ == '__main__':
    a = float(input('a:'))
    print('sigmoid({:.2f})={:.4f}'.format(a, sigmoid(a)))