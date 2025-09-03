weigth = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weigth / (height ** 2)
bmi_rounded = round(bmi)
print(f"Your BMI is: {bmi_rounded}")