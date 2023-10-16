print("Welcome to the tip calculator")

bill = float(input("What is the total bill? $"))
tip = float(input("What percentage would you like to tip? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill = bill * (1 + tip/ 100)
bill_per_person = round(total_bill / people, 2) 

#formats the num to show 2 decimal places, even tho there is only 1 decimal
final_amount = "{:.2f}".format(bill_per_person)
message = f"Each person should pay: ${bill_per_person}"


print(message)

#prints with an additional zero bc of the formatting 
print(f"Each person should pay: ${final_amount}")