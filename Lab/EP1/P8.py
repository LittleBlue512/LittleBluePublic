"""
Student's name: Chattipoom Sirimul
id: 623040132-7
P8
Write a program to ask a user for his/her sleeping duration (in hour),
if it is less than 7, say "You need more rest."
If it is between 7 and 9, say "Good for you."
If it is more than 9, say "Don't you think it's too much?"
And, say "Thank you." before finishing the program.
"""

if __name__ == '__main__':

    # Write your program here
    # ... use the provided string as required
    hr = int(input('How many hours do you sleep a night (in hours)? '))
    
    if hr < 7:
        print("You need more rest.")
    elif hr <= 9:
        print("Good for you.")
    else:
        print("Don't you think it's too much?")

    print("Thank you.")