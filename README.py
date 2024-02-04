# Assignment-CSS-Option-1
CSS Project - Option 1: IMDB Data
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 23:39:36 2024

@author: tebog
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("movie_dataset.csv")

print(df)
df.head()
df.tail()
df.info()
df.nunique()
df.isnull().sum()
(df.isnull().sum()/(len(df)))*100

df.describe().T
df.describe(include='all').T

cat_cols = df.select_dtypes(include=['object']).columns
num_cols = df.select_dtypes(include=np.number).columns.tolist()
print("Categorical Variables:")
print(cat_cols)
print("Numerical Variables:")
print(num_cols)

for col in num_cols:
    print(col)
    print('Skew :', round(df[col].skew(), 2))
    plt.figure(figsize=(15, 4))
    plt.subplot(1, 2, 1)
    df[col].hist(grid=False)
    plt.ylabel('count')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[col])
    plt.show()

    fig, axes = plt.subplots(3, 2, figsize=(18, 18))
fig.suptitle('Bar plot for all categorical variables in the dataset')
sns.countplot(ax=axes[0, 0], x='Rank', df=df, color='blue',
              order=df['Rank'].value_counts().index)
sns.countplot(ax=axes[0, 1], x='Year', df=df, color='green',
              order=df['Year'].value_counts().index)
sns.countplot(ax=axes[1, 0], x='Runtime', df=df, color='purple',
              order=df['Runtime'].value_counts().index)
sns.countplot(ax=axes[1, 1], x='Rating', df=df, color='red',
              order=df['Rating'].value_counts().index)
sns.countplot(ax=axes[2, 0], x='Votes', df=df, color='orange',
              order=df['Votes'].head(20).value_counts().index)
sns.countplot(ax=axes[2, 1], x='Revenue', df=df, color='brown',
              order=df['Revenue'].head(20).value_counts().index)
sns.countplot(ax=axes[2, 2], x='Metascore', df=df, color='yellow',
              order=df['Metascore'].head(20).value_counts().index)
axes[1][1].tick_params(labelrotation=45)
axes[2][0].tick_params(labelrotation=90)
axes[2][1].tick_params(labelrotation=90)

def log_transform(data,col):
    for colname in col:
        if (df[colname] == 1.0).all():
            df[colname + '_log'] = np.log(df[colname]+1)
        else:
            df[colname + '_log'] = np.log(df[colname])
    df.info()
    
    print(df["movie_dataset"].value_counts().sort_values())

    

