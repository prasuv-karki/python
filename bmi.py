height = float(input("Enter your height/cm "))
weight = float(input("Enter your weight/kg: "))
bmi = int(weight / (height/100)**2)
print(f"Your BMI is {bmi}")
