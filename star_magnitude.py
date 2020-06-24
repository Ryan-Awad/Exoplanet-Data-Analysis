import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dataset = input("Dataset: ")

magnitude = pd.read_csv("datasets/" + dataset, sep=',')
sns.set(style="ticks")

f, ax = plt.subplots(figsize=(7, 6))
ax.set_xscale("linear")

sns.lineplot(x="Time", y="Magnitude", data=magnitude)
sns.scatterplot(x="Time", y="Magnitude", data=magnitude) 

sns.despine(trim=True, left=True)
plt.show()