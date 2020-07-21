import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    Tip=meal_cost*0.01*tip_percent
    Tax=meal_cost*0.01*tax_percent
    TotalCost=Tip+Tax+meal_cost
    print(round(TotalCost))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
