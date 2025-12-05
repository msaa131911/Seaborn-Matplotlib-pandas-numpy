import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data=sns.load_dataset('tips')
print(data)
#hue="time", linewidth=2,palette="Dark2"
sns.violinplot(x='time',y='total_bill',data=data,
               order=["Dinner","Lunch"],hue="sex",
               split=True,scale="count",inner="quart")
plt.show()
 