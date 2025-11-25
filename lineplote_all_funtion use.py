import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

arr_1=np.array([40,50,60,70,80]) # array
arr_2=np.array([4,9,6,7,8])#array

# github csv file input
arr_3=sns.load_dataset("penguins").head(20) 



# array ar data fram 
data=pd.DataFrame({"arr_1":arr_1,"arr_2":arr_2}) 

#seaborn lineplot use all function
sns.lineplot(x="bill_length_mm",y="bill_depth_mm",data=arr_3,hue="sex",size=10,style="sex",
             palette="Accent",markers=['o','>'],dashes=True,legend="full")

#np.array
#plt.plot(arr_1,arr_2)

#gride
plt.grid(axis="y",color="green",alpha=0.5,linestyle="--")
plt.grid(axis="x",color="blue",alpha=0.5,linestyle="--")

plt.title("matplotlib + seaborn")

plt.show()


