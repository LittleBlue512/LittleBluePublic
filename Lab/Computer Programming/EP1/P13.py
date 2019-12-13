"""
Student's name: Chattipoom Sirimul
id: 623040132-7
P13
Write a program to calculate a maximum current through a machine.
Given a machine operating at 220 volt,
ask a user for its maximum power consumption,
calculate its maximum current, and report the calculation.
Note: (max current) = (max power)/(operating volt).
"""

if __name__ == '__main__':

    # Write your code here ....
    # ....
    max_power = int(input("Max power:"))
    i = max_power/220

    print('At 220 V, max current = %.4f A'%i) # Keep this line untouched


