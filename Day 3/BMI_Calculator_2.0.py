weight = float(input("What is your weight in Kg? "))
height = float(input("What is your height in m? "))

bmi = round(weight / height**2, 2) 
if bmi < 18.5:
    message = ", You are under weight."
elif bmi < 25:
    message = ", You have a normal weight."
elif bmi < 30:
    message = ", You are overweight."
elif bmi < 35:
    message = ", You are obese."
else:
    message = ", You are clinically obese."

print(f"Your BMI is: {bmi} {message}")