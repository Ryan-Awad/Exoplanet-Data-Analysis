import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dataset = input("Dataset: ")
x_value = input("X: ")
y_value = input("Y: ")

planets = pd.read_csv(dataset, sep=',')
sns.set(style="ticks")

f, ax = plt.subplots(figsize=(7, 6))
ax.set_xscale("log") # you can use "log" which increments the x-axis by multiplying it by 10. Ex: 10^0, 10^1, 10^2, 10^3, 10^4, ..

# Load the example planets dataset
#planets = sns.load_dataset("planets")

# replace pl_pnum and st_mass with other column names
sns.boxplot(x=x_value, y=y_value, data=planets) 

# Add in points to show each observation
sns.swarmplot(x=x_value, y=y_value, data=planets, color=".3", size=2, linewidth=0)
# Tweak the visual presentation

ax.xaxis.grid(True)
sns.despine(trim=True, left=True)
plt.show()