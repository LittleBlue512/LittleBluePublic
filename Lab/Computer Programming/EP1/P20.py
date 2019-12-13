"""
Student's name: Chattipoom Sirimul
id: 623040132-7
P20
Diatonic notes on scale.
Print all diatonic notes on scale, given the scale key.
"""

from P20aux import print_scale # Keep this untouched

# Make the diatonic function work

def diatonic(scale_key):
    scale_key -= 1
    n1 = (scale_key)%12
    n2 = (n1 + 2)%12
    n3 = (n2 + 2)%12
    n4 = (n3 + 1)%12
    n5 = (n4 + 2)%12
    n6 = (n5 + 2)%12
    n7 = (n6 + 2)%12

    return n1+1, n2+1, n3+1, n4+1, n5+1, n6+1, n7+1

# Do not edit below this line.
# ------------------------------------------

if __name__ == "__main__":

    key_of = int(input('Enter the key [1-12]:'))
    k1, k2, k3, k4, k5, k6, k7 = diatonic(key_of)
    print_scale(k1, k2, k3, k4, k5, k6, k7)
    if key_of == 7:
        s = __doc__
        sname = s.split('P20')[0]
        print(sname)

