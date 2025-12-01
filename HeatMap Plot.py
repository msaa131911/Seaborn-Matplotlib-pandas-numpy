import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#data=sns.load_dataset("anagrams").head(10)
var=np.linspace(1,10,10).reshape(2,5)
#sns.heatmap(var)
#x=data.drop(columns="attnr",axis=1)
arr=np.array([["a0","a1","a2","a3","a4"],
             ["b0","b1","b2","b3","a4"]])
#print(x)
v=sns.heatmap(var,vmin=0,vmax=12,cmap="gist_heat",annot=arr,fmt='s',linewidths=10,
            linecolor="r",cbar=False,xticklabels=False,yticklabels=False,)
v.set(xlabel="python",ylabel="c++")
sns.set(font_scale=5)
plt.show()

