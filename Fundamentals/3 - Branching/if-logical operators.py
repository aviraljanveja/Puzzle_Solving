# Logical operators like and, or and not can be used to combine multiple conditions

x = 10
y = 20

if x > 5 and y > 15:
    print("Both conditions are True")

if x > 15 or y > 15:
    print("At least one condition is True")

if not x < 5:
    print("x is not less than 5")
