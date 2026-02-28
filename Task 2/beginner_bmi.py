# Beginner BMI Calculator (Command Line Version)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("===== BMI Calculator (Beginner Version) =====")

    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        if weight <= 0 or height <= 0:
            print("❌ Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("❌ Please enter valid numeric values.")

if __name__ == "__main__":
    main()