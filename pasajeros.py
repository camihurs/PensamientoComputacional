import seaborn as sns
import matplotlib.pyplot as plt

vuelos = sns.load_dataset("flights")
vuelos = vuelos.pivot(index = "month", columns = "year", values = "passengers")
ax = sns.heatmap(vuelos)
plt.show()