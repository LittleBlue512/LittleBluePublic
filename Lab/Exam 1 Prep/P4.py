"""
Student's name: Chattipoom Sirimul
id: 623040132-7
P4
Write a program to ask a user for his/her weight (in kg),
convert it to weights in English unit (lbs) and in Thai unit (Chang),
and report them back.
Note: 1 Chang = 1.2 kg; 1 kg = 2.2 lbs.
"""

if __name__ == '__main__':

    # Write your program here
    kg = int(input('What is your weight (in kg)? '))

    chang = kg/1.2 # dummy answer
    lbs = 2.2*kg # dummy answer

    print("Your weight is %.2f chang or %.2f lbs"%(chang, lbs))