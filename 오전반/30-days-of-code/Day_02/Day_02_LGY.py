#explanation의 식대로 함.
meal_cost = float(input()) #12.00
tip_percent = int(input()) #20
tip_cost = meal_cost * tip_percent/100 #2.4

tax_percent = int(input()) #8
tax_cost = meal_cost * tax_percent/100 #0.96

total_cost = meal_cost + tip_cost + tax_cost #15.36
print(round(total_cost)) #15
