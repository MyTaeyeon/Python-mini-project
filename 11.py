def calculate_bmi(weight_kg, height_m):
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError('Weight and height must be positive values.')
    
    bmi = weight_kg / (height_m**2)
    return bmi

def interpret_bmi(bmi):
    if bmi <18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return "Nomal weight"
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obese'

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi_result = calculate_bmi(weight, height)
interpretation = interpret_bmi(bmi_result)

print(f'Your BMI is: {bmi_result:.2f} - interpretation: {interpretation}')