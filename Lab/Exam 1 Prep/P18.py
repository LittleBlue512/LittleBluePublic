"""
Student's name: Chattipoom Sirimul
id: 623040132-7
P18
Relu
"""

# !!! Write your function here !!!

def relu(a):
    if a > 0:
        return a
    else:
        return 0

# Do not edit below this line
# ===================================
if __name__ == '__main__':
    a = float(input('a:'))
    print('relu({:.2f})={:.4f}'.format(a, relu(a)))