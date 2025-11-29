import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

order_1=["Biscoe","Torgersen"]

df=sns.load_dataset("penguins").head(21)

# hue_order=["Female","Male"] , ci=10, n_boot=3 , color="r", saturation=0.5 

sns.barplot(x="island",y="bill_length_mm",data=df,hue="sex",order=order_1,
            palette="pastel",saturation=0.5,errcolor="b",errwidth=2.5,dodge=False,)

 
#vertical
#sns.barplot(x="bill_depth_mm",y="bill_length_mm",data=df,orient="h") #horizontal,vertical
plt.show()