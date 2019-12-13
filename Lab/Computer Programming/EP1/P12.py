"""
Student's name: Chattipoom Sirimul
id: 623040132-7
P12
Food consumption.
"""

if __name__ == '__main__':
    sex = input('Are you male(M) or female(F)?')

    # Write your code here
    food_kcal = 0
    while True:
        food_name = input("Food:")
        val = int(input("est. kcal:"))
        food_kcal += val
        if (sex is 'M' and food_kcal >= 2500) or (sex is 'F' and food_kcal >= 2000):
            break

    print('That is', food_kcal)
    print("That would be it for your daily diet.")
    print("Be moderate on your diet. Stay healthy.")
