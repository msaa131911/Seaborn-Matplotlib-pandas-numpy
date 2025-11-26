import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=sns.load_dataset("penguins")
sns.displot(data["bill_length_mm"],bins=[35,40,45,50,55,60,65],
            kde=True,rug=True,color="green",log_scale=True)
plt.show()