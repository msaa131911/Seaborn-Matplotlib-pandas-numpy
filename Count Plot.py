from typing_extensions import Pattern
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset("tips")

sns.countplot(x="sex",data=data,hue="smoker",palette="bwr",color="red",saturation=0.1)
plt.show()


