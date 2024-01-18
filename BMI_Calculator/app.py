def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100  # Convert height to meters
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):

    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obese'

def main():
    try:
        height_cm = float(input('Enter your height in centimeters: '))
        weight_kg = float(input('Enter weight in kilograms: '))
    except ValueError:
        print('Invalid input. Please enter valid numerical values for height and weight.')
        return

    bmi = calculate_bmi(height_cm, weight_kg)
    category = interpret_bmi(bmi)

    print('Your BMI is: {:.2f}'.format(bmi))
    print('You are in the "{}" category.'.format(category))

if __name__ == "__main__":
    main()
