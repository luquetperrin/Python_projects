# Take input from the user

height = float(input("Enter your height in meter: \n"))
weight = float(input("Enter your weight in kg: \n"))

# Calculate BMI

bmi = weight / height ** 2
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f} and you are Underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi:.2f} and you are Normal.")
elif bmi < 30:
    print(f"Your BMI is {bmi:.2f} and you are Overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi:.2f} and you are Obese.")
elif bmi < 40:
    print(f"Your BMI is {bmi:.2f} and you are Severely obse.")
else:
    print(f"Your BMI is {bmi:.2f} and you are Morbidly obese.")