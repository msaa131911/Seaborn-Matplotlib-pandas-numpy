import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

m={"Male":"*","Female":"o"}
df=sns.load_dataset("penguins")
sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=df,hue="sex",
                style="sex",size="sex",sizes=(20,200),palette="gist_ncar",
                alpha=0.5,markers=m)
plt.show()
