# Nested if statements
# You can place if statements inside other if statements for more complex conditions.

x = 15
if x > 0:
    print("Positive")
    if x % 5 == 0:
        print("...and divisible by 5")
else:
    print("Non-Positive")
