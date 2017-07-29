"""

https://www.hackerrank.com/challenges/30-operators

"""

mealCost = float(input())
tipPercent = float(input())
taxPercent = float(input())

tipCost = mealCost * (tipPercent / 100)
taxCost = mealCost * (taxPercent / 100)

totalCost = mealCost + tipCost + taxCost
totalCostInInt = round(totalCost)

print("The total meal cost is " + str(totalCostInInt) + " dollars.")
