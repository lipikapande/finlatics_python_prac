import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# df = pd.read_csv(r'C:\Users\Lipika Pande\Downloads\titanic (1).csv')
df = sns.load_dataset('titanic')
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

# to separate passengers based on gender and then count how many survived
grouped_data=df.groupby(['sex','survived'])['survived'].count()

#survival by passenger class
class_survival=df.groupby(['pclass','survived'])['survived'].count()

#visualisation
# sns.countplot(x='sex',hue='survived',data=df)
# plt.show()

# sns.catplot(x='embark_town',hue='survived',col='pclass',data=df,kind='count',palette='Set2')
# plt.show()

#to fill missing values
df['age']=df['age'].fillna(df['age'].median())
df['deck']=df['deck'].fillna(df['deck'].mode()[0])

#correlation matrix
numeric_df=df.select_dtypes(include=['int64','float64'])
corr_matrix=numeric_df.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix,annot=True,cmap='PuBuGn',fmt='.2f')
# plt.show()