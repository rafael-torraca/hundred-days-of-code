from random import randint

dice_images = ["A", "B", "C", "D", "E", "F"]
dice_num = randint(0,5)
print(dice_num)
print(dice_images[dice_num])


year = int(input("What's your year of birth? "))

if year > 1980 and year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")
