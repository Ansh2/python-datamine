print("Hello World!")

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter an integer: "))
print("The sum of the two numbers is: " + str(num1 + num2))

myfruits = []
for i in range(1, 6):
    myfruits.append(input(f"Name of Fruit {i}: "))
print(myfruits)

import pandas as pd
forest = pd.read_csv("/anvil/projects/tdm/data/forest/ENTIRE_COUNTY.csv")
forest.info()
forest.shape
forest.size
forest.columns
len(forest.columns)