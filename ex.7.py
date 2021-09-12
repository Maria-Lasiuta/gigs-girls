meal = float(input("Enter your meal amount: "))
tip = int(input("Enter your tip %: "))

tip_amt = meal * tip/100
total = meal + tip_amt
print(f"Your meal was {meal} and your tip was {tip_amt}.")
print(f"Your total with tip was {total}.")
