# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# # My attempt
# death_age = 90
# days_in_a_year = 365
# weeks_in_a_year = 52
# months_in_a_year = 12

# new_born_remaining_days = death_age * days_in_a_year
# new_born_remaining_weeks = death_age * weeks_in_a_year
# new_born_remaining_months = death_age * months_in_a_year

# current_age = int(input("What is your current age? "))

# days_lived = current_age * days_in_a_year
# weeks_lived = current_age * weeks_in_a_year
# months_lived = current_age * months_in_a_year

# days_remaining = new_born_remaining_days - days_lived
# weeks_remaining = new_born_remaining_weeks - weeks_lived
# months_remaining = new_born_remaining_months - months_lived

# print(f"You have remaining {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months to live")




# improved code
death_age = 90
days_in_a_year = 365
weeks_in_a_year = 52
months_in_a_year = 12

current_age = int(input("What is your current age? "))
remaining_years = death_age - current_age
remaining_days = remaining_years * days_in_a_year
remaining_weeks = remaining_years * weeks_in_a_year
remaining_months = remaining_years * months_in_a_year

print(f"You have remaining {remaining_days} days, {remaining_weeks} weeks, {remaining_months} months to live")