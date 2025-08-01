#code implementation
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df=pd.read_csv('diabetes.csv')
df.head()

df.shape

df.info()

df["BMI"]=df["BMI"].astype(np.int64)

df.info()

df["BMI"].fillna(df["BMI"].mean(),inplace=True)

# Box Plot
import seaborn as sns
sns.boxplot(df['Insulin'])

from os import remove
import seaborn as sns
import matplotlib.pyplot as plt


def removal_box_plot(df, column, threshold1,threshold2):
    sns.boxplot(df[column])
    plt.title(f'Original Box Plot of {column}')
    plt.show()

    removed_outliers = df[df[column] <= threshold1]
    removed_outliers=removed_outliers[removed_outliers>threshold2]

    sns.boxplot(removed_outliers[column])
    plt.title(f'Box Plot without Outliers of {column}')
    plt.show()
    return removed_outliers


threshold_value = 0.12

no_outliers = removal_box_plot(df,'BMI',49,15)

df.corr()

x,y=df.iloc[:,:7],df.iloc[:,8]
x.head()

y.head()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# Standardize features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(x_train,y_train)

y_pred=model.predict(x_test)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc

x=accuracy_score(y_test,y_pred)
print(x)

import seaborn as sns
sns.heatmap(confusion_matrix(y_test,y_pred),annot=True)

sns.heatmap(x.corr(),annot=True)
