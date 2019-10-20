"""
Student's Name: !!!Write your name here!!!
ID: !!!Write your id here!!!
P20
Diatonic notes on scale.
Print all diatonic notes on scale, given the scale key.
"""

from P20aux import print_scale # Keep this untouched

# Make the diatonic function work

def diatonic(scale_key):

    # Fix this to work on all keys
    # Hint: recall the triad exercise question
    n1 = 1 # has to be fixed
    n2 = 3 # has to be fixed
    n3 = 5 # has to be fixed
    n4 = 6 # has to be fixed
    n5 = 8 # has to be fixed
    n6 = 10 # has to be fixed
    n7 = 12 # has to be fixed

    return n1, n2, n3, n4, n5, n6, n7

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

