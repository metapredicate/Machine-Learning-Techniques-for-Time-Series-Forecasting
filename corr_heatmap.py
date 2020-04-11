import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("C:\Users\hurri\Desktop\SWENG\Data\Appliances Energy Usage Prediction\energydata_complete.csv", index_col = 0)
df.head()

#CALCULATE CORRELATION MATRIX
corr_matrix = df.corr()
corr_matrix

#df_dummy = pd.get_dummies(df.date) 
#df_dummy
#df = pd.concat([df, df_dummy], axis = 1)

corr_matrix = df.corr()

#SET UP MASK TO HIDE UPPER TRIANGLE
np.zeros_like(corr_matrix)
np.zeros_like(corr_matrix, dtype=np.bool)
mask = np.zeros_like(corr_matrix, dtype=np.bool)
np.triu_indices_from(mask) #Return the indices for the upper-triangle of array
mask[np.triu_indices_from(mask)]= True


#CREATE HEATMAP IN SEABORN
f, ax = plt.subplots(figsize=(12, 17)) 
heatmap = sns.heatmap(corr_matrix, 
                      mask = mask,
                      square = True,
                      linewidths = .3,
                      cmap ='coolwarm',
                      cbar_kws={"shrink": .4, 'ticks' : [-1, -.5, 0, 0.5, 1]},
                      vmin = -1, 
                      vmax = 1,
                      annot = True,
                      annot_kws = {"size": 6})
ax.set_yticklabels(corr_matrix.columns, rotation = 0)
ax.set_xticklabels(corr_matrix.columns) #add the column names as labels
sns.set_style({'xtick.bottom': True}, {'ytick.left': True})

heatmap;

heatmap.get_figure().savefig('C:\Users\hurri\Desktop\SWENG\heatmap7.png', bbox_inches='tight') #I found that bbox_inches = 'tight' helps your picture not get cut off if it's too big