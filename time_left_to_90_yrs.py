age = input("What is your current age?")

age_as_int = int(age)

years_left = int(90 - age_as_int)

days_left = 365 * years_left
weeks_left = 52 * years_left
months_left = 12 * years_left

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months left.")
