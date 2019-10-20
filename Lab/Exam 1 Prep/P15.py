"""
Student's name: Chattipoom Sirimul
id: 623040132-7
P15
Write a program to calculate a lasting duration of a mobile phone battery.
Ask a user for battery energy storage (in Wh),
the phone average power consumptions (in mW) in idle
and in normal operation,
then calculate estimate duration time the battery will last in each mode,
and report the results.
Note: 1 W = 1000 mW;
(Energy Wh) = (Average Power in W) * (Operating time in hr)
"""

if __name__ == '__main__':

    # Write your code here ....
    # ....
    w = int(input("Battery capacity (Wh):"))
    w_idle = int(input("average power (idle, mW):"))
    w_norm = int(input("average power (normal, mW):"))
    w_idle = w_idle/1000
    w_norm = w_norm/1000
    d_idle = w/w_idle
    d_norm = w/w_norm


    # Don't edit below this line.
    # ================================================================
    print('The battery will last %.0f hrs in idle mode.'%d_idle)
    print('The battery will last %.1f hrs in normal mode.'%d_norm)
