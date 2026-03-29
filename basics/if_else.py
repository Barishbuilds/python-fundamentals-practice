# Operators in Python
# Arithmetic operators: +, -, *, /, //, %, **
# Comparison operators: ==, !=, <, >, <=, >=
# Logical operators: and, or, not


# Basic if-else statement
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# If-elif-else statement
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")


# Logical operators in if-else statements
age = 23
has_license = False

# and operator
if age >= 18 and has_license:
    status = "You can drive."
else:
    status = "You cannot drive."
print(status)

# or operator
if age >= 18 or has_license:
    status = "You can drive."
else:
    status = "You cannot drive."
print(status)

# not operator
if not has_license:
    status = "You cannot drive."
else:
    status = "You can drive."
print(status)


# Productivity checker
total_productive_hours = (
    float(input("Enter your productive hours for Monday: ")) +
    float(input("Enter your productive hours for Tuesday: ")) +
    float(input("Enter your productive hours for Wednesday: ")) +
    float(input("Enter your productive hours for Thursday: ")) +
    float(input("Enter your productive hours for Friday: ")) +
    float(input("Enter your productive hours for Saturday: ")) +
    float(input("Enter your productive hours for Sunday: "))
)

average_hours = total_productive_hours / 7

if average_hours >= 10:
    status = "Excellent. This shows strong discipline and consistency."
elif average_hours >= 7:
    status = "Good. You are doing well, but there is still room to improve."
elif average_hours >= 4:
    status = "Average. You need to become more consistent."
else:
    status = "You need to improve your daily productivity."

print(f"Your total productive hours in a week: {total_productive_hours}")
print(f"Your average productive hours in a day: {average_hours}")
print(status)


# Voting eligibility checker
person_age = int(input("Enter your age: "))

if person_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")