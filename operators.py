import math
def solve(meal_cost, tip_percent, tax_percent):
    tip=(meal_cost/100)*tip_percent
    tax=(tax_percent/100)*meal_cost
    total_cost=meal_cost+tip+tax
    print(round(total_cost))
solve(float(input()),int(input()),int(input()))
