import numpy as np

die_sides=int(input("enter number of sides (6/12):"))
die=range(1,die_sides)

num_rolls=int(input("enter number of times you want to roll dice :"))

results=np.random.choice(die,size=num_rolls,replace=True)
print(results)