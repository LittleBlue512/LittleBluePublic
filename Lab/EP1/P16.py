"""
Student's name: Chattipoom Sirimul
id: 623040132-7
P16
Write a program to calculate an energy storage (in kilo calories, kcal) to Joules (J), and Watt-hour (Wh).
Note 1Wh = 3600 J; 1 kcal = 4184 J;
"""

if __name__ == '__main__':

    # Write your code here ...
    # ...
    cal = int(input("Energy( in kcal):"))
    J = 4184*cal
    Wh = J/3600

    print("That is {:.2f} J or {:.2f} Wh.".format(J, Wh)) # Leave this line untouched
