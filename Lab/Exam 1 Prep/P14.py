"""
Student's name: Chattipoom Sirimul
id: 623040132-7
P14
Write a program to calculate an energy stored in a battery.
Given a battery operating at 12 volt, ask a user for its capacity (in mAh),
calculate its energy stored (in Wh), and report the calculation.
Note: 1 Ah = 1000 mAh; and
(Energy in Wh) = (capacity in Ah) * (operating volt in V).
"""

if __name__ == '__main__':

    # Write your code here ....
    # ....
    cap = int(input("Battery capacity (mAh):"))
    cap = cap/1000
    Wh = cap*12

    # Don't edit below this line.
    # ================================================================
    print('At its 12 V rating, it stores %.2f Wh.'%Wh)
