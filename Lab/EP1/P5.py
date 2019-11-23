"""
Student's name: Chattipoom Sirimul
id: 623040132-7
Write a program to ask a user for his/her height (in cm),
convert it to feet (ft) and inches (in) and report them back.
Note 2.54 cm = 1 in; 12 in = 1 ft.
"""

if __name__ == '__main__':

    # Write your program here
    # Use the texts provided as fit

    cm = int(input('How tall are you (in cm)? '))

    feet = cm//(12*2.54)
    cm = cm - feet*12*2.54
    inch = cm/2.54

    # Do not edit below this line.
    # ------------------------------------------------------
    print("That is around %d ft %d in."%(feet, round(inch)))